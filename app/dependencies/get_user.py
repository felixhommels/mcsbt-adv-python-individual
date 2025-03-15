from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.database import get_db
import jwt
from app.core.security import SECRET_KEY, ALGORITHM

async def get_current_user(token: str = Header(None), db: Session = Depends(get_db)) -> User:
    if not token:
        raise HTTPException(status_code=401, detail="Missing API Token")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user