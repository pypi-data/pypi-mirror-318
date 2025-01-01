import time
from fastapi import Request
from sqlalchemy.orm import  Session
from starlette.middleware.base import BaseHTTPMiddleware
from harlequelrah_fastapi.middleware.crud_middleware import save_log
class LoggerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app,LoggerMiddlewareModel, session_factory ):
        super().__init__(app)
        self.session_factory=session_factory
        self.LoggerMiddlewareModel = LoggerMiddlewareModel
    async def dispatch(self, request : Request, call_next):
        try:
            db=self.session_factory()
            return await save_log(request=request,call_next=call_next,LoggerMiddlewareModel=self.LoggerMiddlewareModel,db=db)
        except Exception as e:
            db.rollback()
            return await save_log(request, call_next=call_next,LoggerMiddlewareModel= self.LoggerMiddlewareModel, db=db,error=f"error during saving log , detail :{str(e)}")
        finally:
            db.close()
