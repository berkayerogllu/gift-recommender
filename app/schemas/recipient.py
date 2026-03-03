from pydantic import BaseModel
from typing import List, Optional

class RecipientBase(BaseModel):
    name: str
    relationship_type: str
    interests: List[str] 

class RecipientCreate(RecipientBase):
    user_id: int 

class RecipientUpdate(BaseModel):
    name: Optional[str] = None
    relationship_type: Optional[str] = None
    interests: Optional[List[str]] = None

class RecipientRead(RecipientBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True