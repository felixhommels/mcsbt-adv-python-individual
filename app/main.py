from fastapi import FastAPI
from app.core.database import Base, engine
from app.routes import auth, expenses
import uvicorn

app = FastAPI(
    title="Expense Tracker API",
    description="API which allows users to track and view their expenses"
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(expenses.router, prefix="/expenses", tags=["Expenses"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Expense Tracker API"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

