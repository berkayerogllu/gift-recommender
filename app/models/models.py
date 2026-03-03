from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship

from app.db.session import Base

class User(Base):
  __tablename__= "users"
  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, unique=True , index=True , nullable=False)
  hashed_password = Column(String , nullable = False)
  recipients = relationship("Recipient", back_populates="owner")

class Recipient(Base):
  __tablename__= "reciepents"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  relationship_type = Column(String)     
  interests = Column(JSON)            
  user_id = Column(Integer, ForeignKey("users.id"))
  owner = relationship("User", back_populates="recipients")