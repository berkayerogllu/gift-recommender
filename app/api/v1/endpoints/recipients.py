from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db.session import get_db
from app.schemas.recipient import RecipientCreate, RecipientRead, RecipientUpdate
from app.services import recipient_service

router = APIRouter()

@router.post("/", response_model=RecipientRead)
async def create_recipient(recipient: RecipientCreate, db: AsyncSession = Depends(get_db)):
    return await recipient_service.create_recipient(db=db, recipient=recipient)

@router.get("/user/{user_id}", response_model=List[RecipientRead])
async def get_recipients_by_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await recipient_service.get_recipients_by_user(db=db, user_id=user_id)

@router.get("/{recipient_id}", response_model=RecipientRead)
async def get_recipient(recipient_id: int, db: AsyncSession = Depends(get_db)):
    db_recipient = await recipient_service.get_recipient(db=db, recipient_id=recipient_id)
    if db_recipient is None:
        raise HTTPException(status_code=404, detail="Recipient not found")
    return db_recipient

@router.put("/{recipient_id}", response_model=RecipientRead)
async def update_recipient(recipient_id: int, recipient: RecipientUpdate, db: AsyncSession = Depends(get_db)):
    db_recipient = await recipient_service.update_recipient(db=db, recipient_id=recipient_id, recipient_data=recipient)
    if db_recipient is None:
        raise HTTPException(status_code=404, detail="Recipient not found")
    return db_recipient

@router.delete("/{recipient_id}")
async def delete_recipient(recipient_id: int, db: AsyncSession = Depends(get_db)):
    success = await recipient_service.delete_recipient(db=db, recipient_id=recipient_id)
    if not success:
        raise HTTPException(status_code=404, detail="Recipient not found")
    return {"message": "Recipient deleted successfully"}