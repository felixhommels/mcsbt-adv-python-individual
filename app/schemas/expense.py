from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import date

class ExpenseCategory(str, Enum):
    FOOD = "FOOD"
    TRANSPORTATION = "TRANSPORTATION"
    ENTERTAINMENT = "ENTERTAINMENT"
    INVESTMENT = "INVESTMENT"
    OTHER = "OTHER"

class ExpenseBase(BaseModel):
    amount: float
    description: Optional[str] = Field(None, min_length=3, max_length=200)
    category: ExpenseCategory
    created_at: Optional[date] = Field(default_factory=date.today)

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseResponse(ExpenseBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class ExpenseList(BaseModel):
    id: int
    amount: float
    description: Optional[str] = Field(None, min_length=3, max_length=200)
    category: ExpenseCategory
    created_at: date

    class Config:
        orm_mode = True
    
class ExpenseResponseDetail(ExpenseResponse):
    amount: float
    description: Optional[str] = Field(None, min_length=3, max_length=200)
    category: ExpenseCategory
    created_at: date
    message: Optional[str] = Field(None)

    class Config:
        orm_mode = True
    
    
