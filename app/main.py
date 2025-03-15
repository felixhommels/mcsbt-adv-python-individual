from fastapi import FastAPI
from core.database import Base, engine
from routes import auth
import uvicorn

app = FastAPI(
    title="Expense Tracker API",
    description="API which allows users to track and view their expenses"
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Expense Tracker API"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

