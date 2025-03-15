from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate, ExpenseResponse, ExpenseList, ExpenseResponseDetail, ExpenseCategory
from app.models.user import User
from typing import List
from app.dependencies.get_user import get_current_user

router = APIRouter()

@router.post("/", response_model=ExpenseResponse)
async def create_expense(expense: ExpenseCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    expense_data = Expense(**expense.dict(), user_id=current_user.id)
    db.add(expense_data)
    db.commit()
    db.refresh(expense_data)
    return expense_data

@router.get("/", response_model=List[ExpenseList])
async def get_expenses(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    expenses = db.query(Expense).filter(Expense.user_id == current_user.id).all()
    return expenses

@router.get("/id-get/{expense_id}", response_model=ExpenseResponseDetail)
async def get_expense(expense_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id, Expense.user_id == current_user.id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

@router.get("/category/{expense_category}", response_model=List[ExpenseList])
async def get_expenses_by_category(expense_category: ExpenseCategory, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    expenses = db.query(Expense).filter(Expense.user_id == current_user.id, Expense.category == expense_category).all()
    return expenses

@router.put("/id-update/{expense_id}", response_model=ExpenseResponseDetail)
async def update_expense(expense_id: int, expense: ExpenseCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    expense_data = db.query(Expense).filter(Expense.id == expense_id, Expense.user_id == current_user.id).first()
    if not expense_data:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    expense_data.amount = expense.amount
    expense_data.description = expense.description
    expense_data.category = expense.category
    expense_data.created_at = expense.created_at
    
    db.commit()
    db.refresh(expense_data)
    
    expense_dict = {
        "id": expense_data.id,
        "amount": expense_data.amount,
        "description": expense_data.description,
        "category": expense_data.category,
        "created_at": expense_data.created_at,
        "user_id": expense_data.user_id,
        "message": "Expense updated successfully"
    }
    
    return expense_dict

@router.delete("/id-delete/{expense_id}", status_code=204)
async def delete_expense(expense_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    expense_data = db.query(Expense).filter(Expense.id == expense_id, Expense.user_id == current_user.id).first()
    if not expense_data:
        raise HTTPException(status_code=404, detail="Expense not found")
    db.delete(expense_data)
    db.commit()
    return {"message": "Expense deleted successfully"}
