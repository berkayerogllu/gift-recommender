from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.models import Recipient
from app.schemas.recipient import RecipientCreate, RecipientUpdate

async def create_recipient(db: AsyncSession, recipient: RecipientCreate):
    db_recipient = Recipient(
        name=recipient.name,
        relationship_type=recipient.relationship_type,
        interests=recipient.interests,
        user_id=recipient.user_id
    )
    db.add(db_recipient)
    await db.commit()
    await db.refresh(db_recipient)
    return db_recipient

async def get_recipient(db: AsyncSession, recipient_id: int):
    result = await db.execute(select(Recipient).filter(Recipient.id == recipient_id))
    return result.scalars().first()

async def get_recipients_by_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(Recipient).filter(Recipient.user_id == user_id))
    return result.scalars().all()

async def update_recipient(db: AsyncSession, recipient_id: int, recipient_data: RecipientUpdate):
    db_recipient = await get_recipient(db, recipient_id)
    if not db_recipient:
        return None
    
    if recipient_data.name is not None:
        db_recipient.name = recipient_data.name
    if recipient_data.relationship_type is not None:
        db_recipient.relationship_type = recipient_data.relationship_type
    if recipient_data.interests is not None:
        db_recipient.interests = recipient_data.interests
        
    await db.commit()
    await db.refresh(db_recipient)
    return db_recipient

async def delete_recipient(db: AsyncSession, recipient_id: int):
    db_recipient = await get_recipient(db, recipient_id)
    if not db_recipient:
        return False
    
    await db.delete(db_recipient)
    await db.commit()
    return True