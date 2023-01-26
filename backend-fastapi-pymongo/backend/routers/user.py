from fastapi import APIRouter, Depends, status
from typing import List

from database import get_db
import crud
import schemas
from auth import get_password_hash, get_user_by_token
import util.user_checks as checks
from util import common

def hash_request(request: schemas.UserCreate|dict) -> dict:
    if type(request) is dict: request_dict = request.copy()
    else: request_dict = request.dict()
    request_dict['hashed_password'] = get_password_hash(request_dict.pop('password'))
    return request_dict

# Routes
router = APIRouter(prefix = '/user', tags = ['users'])

@router.post('/', status_code = status.HTTP_201_CREATED, response_model = schemas.UserRead,
    responses = checks.responses['duplicate'])
def create_user(request: schemas.UserCreate, db = Depends(get_db)):
    checks.duplicate_email(db, request.email)
    checks.duplicate_username(db, request.username)
    return crud.user.create_one(db, hash_request(request))

@router.get('/', response_model = List[schemas.UserRead],
    responses = common.responses['unauthenticated'] | checks.responses['admin'])
def get_all_users(db = Depends(get_db), user = Depends(get_user_by_token)): #limit: int = 10, skip: int = 0): # Pagination
    checks.admin(user)
    return crud.user.read(db) #, sort, limit, skip

@router.get('/me', response_model = schemas.UserRead,
    responses = common.responses['unauthenticated'])
def get_user_me(user = Depends(get_user_by_token)):
    return user

@router.get('/{id}', response_model = schemas.UserRead,
    responses = common.responses['unauthenticated'] | checks.responses['exists'] | checks.responses['me_or_admin'])
def get_user_by_id(id: int, db = Depends(get_db), user = Depends(get_user_by_token)):
    target = crud.user.read_one(db, {'id': id})
    checks.exists_user(target)
    checks.me_or_admin(user, id)
    return target

@router.put('/{id}', response_model = schemas.UserRead,
    responses = common.responses['unauthenticated'] | checks.responses['exists'] | checks.responses['me_or_admin'] | checks.responses['duplicate'])
def update_user(id: int, request: schemas.UserUpdate, db = Depends(get_db), user = Depends(get_user_by_token)):
    target = crud.user.read_one(db, {'id': id})
    checks.exists_user(target)
    checks.me_or_admin(user, id)
    if request.username: checks.duplicate_username(db, request.username)
    if request.email: checks.duplicate_email(db, request.email)
    return crud.user.update(hash_request(request))

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT,
    responses = common.responses['unauthenticated'] | checks.responses['exists'] | checks.responses['me_or_admin'])
def delete_user(id: int, db = Depends(get_db), user = Depends(get_user_by_token)):
    target = crud.user.read_one(db, {'id': id})
    checks.exists_user(target)
    checks.me_or_admin(user, id)
    return crud.user.delete(db, {'id': id})