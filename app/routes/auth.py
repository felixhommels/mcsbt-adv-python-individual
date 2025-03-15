from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import hash_password, create_access_token, verify_password
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = hash_password(user.password)
    user_data = User(name=user.name, email=user.email, hashed_password=hashed_password)
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    
    return UserResponse(
        id=user_data.id,
        name=user_data.name,
        email=user_data.email,
        message="User registered successfully"
    )

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token({"sub": user.email, "id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
