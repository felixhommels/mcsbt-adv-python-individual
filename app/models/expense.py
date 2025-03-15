from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base
from enum import Enum as PyEnum

class ExpenseCategory(PyEnum):
    FOOD = "food"
    TRANSPORTATION = "transportation"
    ENTERTAINMENT = "entertainment"
    INVESTMENT = "investment"
    OTHER = "other"

class Expense(Base):
    __tablename__ = "expenses"
    
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    category = Column(Enum(ExpenseCategory), nullable=False)
    created_at = Column(Date, nullable=False)
    
    user = relationship("User", back_populates="expenses")
    