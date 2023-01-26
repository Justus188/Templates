from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from database import get_db
import crud

from auth.hash import verify_password_hash
from auth.schemas import Token
from auth.token import create_token, decode_token
from auth.exceptions import CredentialsException, FailedLoginException

PATH_AUTH = '/login'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = PATH_AUTH[1:])

def get_user_by_token(token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    print(decode_token(token))
    user = crud.user.read_one(db, {'id': decode_token(token)})
    print(user)
    if not user:
        raise CredentialsException
    return user

router = APIRouter(tags = ['auth'])

@router.post(PATH_AUTH, response_model = Token)
def login(request: OAuth2PasswordRequestForm = Depends(), db = Depends(get_db)):
    user = crud.user.read_one(db, {'username': request.username})
    if not user:
        raise FailedLoginException
    if not verify_password_hash(request.password, user['hashed_password']):
        raise FailedLoginException
    return {'access_token': create_token({"sub": user['id']}), 'token_type': 'bearer'}