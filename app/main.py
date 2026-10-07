from fastapi import FastAPI,HTTPException,status
from app.models import ExpenseCreate,ExpenseUpdate,Expense
from app.database import ExpenseDatabase

app=FastAPI(title="SWYNEX Expense Tracker API",description="Production-style expense tracking API.",version="1.0.0")
db=ExpenseDatabase()

@app.get("/")
def root(): return {"message":"SWYNEX Expense Tracker API is running"}

@app.get("/health")
def health(): return {"status":"healthy"}

@app.get("/expenses",response_model=list[Expense])
def get_expenses(): return db.get_all()

@app.get("/expenses/{expense_id}",response_model=Expense)
def get_expense(expense_id:int):
    item=db.get(expense_id)
    if not item: raise HTTPException(404,"Expense not found")
    return item

@app.post("/expenses",response_model=Expense,status_code=status.HTTP_201_CREATED)
def create_expense(expense:ExpenseCreate): return db.create(expense)

@app.put("/expenses/{expense_id}",response_model=Expense)
def update_expense(expense_id:int,expense:ExpenseUpdate):
    item=db.update(expense_id,expense)
    if not item: raise HTTPException(404,"Expense not found")
    return item

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id:int):
    if not db.delete(expense_id): raise HTTPException(404,"Expense not found")
    return {"message":"Expense deleted successfully"}

@app.get("/expenses/summary/total")
def total_expenses(): return {"total":db.total_amount()}
