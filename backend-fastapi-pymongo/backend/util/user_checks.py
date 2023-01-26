from fastapi import HTTPException, status
import crud, schemas

def duplicate_username(db, username: str) -> None:
    if crud.user.read_one(db, {'username': username}):
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = [{'loc': ['body', 'username'], 'msg': f'Username {username} already taken.'}])
def duplicate_email(db, email: str) -> None:
    if crud.user.read_one(db, {'email': email}):
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = [{'loc': ['body', 'email'], 'msg': f'Email {email} already has an account.'}])

def exists_user(user) -> None:
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = [{'msg': f'User with id {id} not found.'}])

def me_or_admin(user, userid: int) -> None:
    if user.role != 'admin' and user.id != userid:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = [{'msg': 'Only admin or target user can access this.'}])
def admin(user) -> None:
    if user.role != 'admin':
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = [{'msg': 'Only admin can access this.'}])

responses = {'duplicate': {400: {'model': schemas.ErrorDetailChildMsgLoc, 'description': 'Bad Request: Username or email already taken.'}},
             'exists': {404: {'model': schemas.ErrorDetailParentMsg, 'description': 'Not Found: Userid not found.'}},
             'admin': {403: {'model': schemas.ErrorDetailParentMsg, 'description': 'Forbidden: Only admin can access this.'}},
             'me_or_admin': {403: {'model': schemas.ErrorDetailParentMsg, 'description': 'Forbidden: Only user or admin can access this.'}}}