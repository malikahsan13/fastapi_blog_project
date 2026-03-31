from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    
class UserLogin(BaseModel):
    email: str
    password: str
    
class UserOut(BaseModel):
    id: int
    username: str
    email: str
    
    class Config:
        orm_mode = True   # Return ORM model completely
        
class PostCreate(BaseModel):
    title: str
    content: str
    
class PostOut(BaseModel):
    id: int
    title: str
    content: str
    author: str
    
    class Config:
        orm_mode = True