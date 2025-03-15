from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import date

class ExpenseCategory(str, Enum):
    FOOD = "food"
    TRANSPORTATION = "transportation"
    ENTERTAINMENT = "entertainment"
    INVESTMENT = "investment"
    OTHER = "other"

class ExpenseBase(BaseModel):
    amount: float
    description: Optional[str] = Field(None, min_length=3, max_length=200)
    user_id: int
    category: ExpenseCategory
    created_at: Optional[date] = Field(default_factory=date.today)

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseResponse(ExpenseBase):
    id: int
    
