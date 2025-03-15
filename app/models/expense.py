from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum, Float
from sqlalchemy.orm import relationship
from app.core.database import Base
from enum import Enum as PyEnum
from datetime import date

class ExpenseCategory(PyEnum):
    FOOD = "FOOD"
    TRANSPORTATION = "TRANSPORTATION"
    ENTERTAINMENT = "ENTERTAINMENT"
    INVESTMENT = "INVESTMENT"
    OTHER = "OTHER"

class Expense(Base):
    __tablename__ = "expenses"
    
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    category = Column(Enum(ExpenseCategory), nullable=False)
    created_at = Column(Date, nullable=False, default=date.today())
    
    user = relationship("User", back_populates="expenses")
    