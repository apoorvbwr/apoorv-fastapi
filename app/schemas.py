from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating: Optional[int] = None
    
class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True

# For Response (In order to get response of our choice we can define it in below class
#  title content and published inherit from PostBase class if I don't want to show Id
# I can remove it from below class)
class Post(PostBase):
    id: int
    created_at: datetime
    ownner_id: int
    owner: UserOut    
    
    class Config:
        orm_mode = True
    
    
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
    
    