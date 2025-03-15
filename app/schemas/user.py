from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    
class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    message: str
    
    class Config:
        orm_mode = True
        
        