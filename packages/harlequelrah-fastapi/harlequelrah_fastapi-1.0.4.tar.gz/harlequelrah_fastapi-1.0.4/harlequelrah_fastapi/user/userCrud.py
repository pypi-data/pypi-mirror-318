from fastapi.responses import JSONResponse
from harlequelrah_fastapi.authentication.authenticate import Authentication
from harlequelrah_fastapi.exception.custom_http_exception import \
    CustomHttpException as CHE
from harlequelrah_fastapi.utility.utils import update_entity
from sqlalchemy import or_
from sqlalchemy.sql import func

from fastapi import Depends
from fastapi import HTTPException as HE
from fastapi import  status


class UserCrud:
    def __init__(self, authentication: Authentication):
        self.authentication = authentication
        self.User = self.authentication.User
        self.UserLoginModel = self.authentication.UserLoginModel
        self.UserCreate = self.authentication.UserCreateModel
        self.UserUpdate = self.authentication.UserUpdateModel

    async def get_count_users(self):
        db=self.authentication.session_factory()
        return db.query(func.count(self.User.id)).scalar()

    async def is_unique(self, sub: str):
        db = self.authentication.session_factory()
        user = (
            db.query(self.User)
            .filter(or_(self.User.email == sub, self.User.username == sub))
            .first()
        )
        return user is None

    async def create_user(self, user):
        db = self.authentication.session_factory()
        new_user = self.User(**user.dict())
        new_user.set_password(new_user.password)
        if not await self.is_unique(new_user.email) or not await self.is_unique(
            new_user.username
        ):
            http_exc = HE(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User already registred",
            )
            raise  CHE(http_exc)
        try :
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
        except HE as e :
            db.rollback()
            http_exc=HE(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error during creating user , detail : {str(e)}")
            raise  CHE(http_exc)
        return new_user

    async def get_user(self,id: int = None,sub: str = None):
        db = self.authentication.session_factory()
        user = (
            db.query(self.User)
            .filter(
                or_(
                    self.User.username == sub,
                    self.User.email == sub,
                    self.User.id == id,
                )
            )
            .first()
        )
        if not user:
            http_exc = HE(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )
            raise CHE(http_exc)
        return user

    async def get_users(
        self,
        skip: int = 0,
        limit: int = None,
    ):
        db = self.authentication.session_factory()
        if limit is None :limit = await self.get_count_users()
        return db.query(self.User).offset(skip).limit(limit).all()

    async def update_user(self,
        user_id: int,
        userUpdated,
    ):
        db = self.authentication.session_factory()
        existing_user = await self.get_user(db, user_id)
        existing_user=update_entity(existing_user, userUpdated)
        try:
            db.commit()
            db.refresh(existing_user)
        except HE as e:
            db.rollback()
            http_exc = HE(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error during updating user, detail : {str(e)}",
            )
            raise CHE(http_exc)
        return existing_user

    async def delete_user(self,user_id:int):
        db = self.authentication.session_factory()
        user = await self.get_user(id=user_id)
        try:
            db.delete(user)
            db.commit()
        except HE as e:
            db.rollback()
            http_exc = HE(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error during deleting user, detail : {str(e)}",
            )
            raise CHE(http_exc)
        return JSONResponse(status_code=200,content={'message': 'User deleted successfully'})
