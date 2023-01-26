from fastapi import HTTPException, status

from crud.base import CRUDBase
import schemas

class CRUDUser(CRUDBase):
    def __init__(self, debug: bool = False):
        super().__init__('users', debug)

user = CRUDUser(debug = True)