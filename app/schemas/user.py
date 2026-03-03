from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
  email: str

class UserCreate(UserBase):
  password: str

class UserUpdate(BaseModel):
  email: Optional[str] = None
  password: Optional[str] = None  

class UserRead(UserBase):
  id: int

class Config:
  from_attributes = True