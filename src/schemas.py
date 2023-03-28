from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]


    class Config:
        orm_mode=True
        schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": "password",
                "is_staff": False,
                "is_active": True
                }
        }


class Settings(BaseModel):
    authjwt_secret_key:str = '0fd308d6548f40f2d7552788ff8c1f6bf9806b1d4ee6fb7943abb3399cadd976'


class LoginModel(BaseModel):
    username:str
    password:str