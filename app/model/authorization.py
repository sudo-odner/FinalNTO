from pydantic import BaseModel, EmailStr
from app.model.model import DateModel

class SessionOutModel(BaseModel):
    session: str

    class Config:
        schema_extra = {
            "example": {
                "session": "5thn2bdi5lwwq41rs45"
            }
        }

class LoginModel(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "examplepassword"
            }
        }
    
class RegistedModel(BaseModel):
    name: str

    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "name": "First Name",
                "email": "user@example.com",
                "password": "examplepassword"
            }
        }