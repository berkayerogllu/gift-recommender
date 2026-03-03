from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.models import User
from app.schemas.user import UserCreate, UserUpdate

async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(email=user.email, hashed_password=user.password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalars().first()

async def get_all_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()

async def update_user(db: AsyncSession, user_id: int, user_data: UserUpdate):
    db_user = await get_user(db, user_id)
    if not db_user:
        return None
    
    if user_data.email is not None:
        db_user.email = user_data.email
    if user_data.password is not None:
        db_user.hashed_password = user_data.password
        
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def delete_user(db: AsyncSession, user_id: int):
    db_user = await get_user(db, user_id)
    if not db_user:
        return False
    
    await db.delete(db_user)
    await db.commit()
    return True