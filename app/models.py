from pydantic import BaseModel,Field
from typing import Optional

class ExpenseCreate(BaseModel):
    title:str=Field(...,min_length=2,max_length=100)
    amount:float=Field(...,gt=0)
    category:str=Field(...,min_length=2,max_length=30)
    description:Optional[str]=Field(None,max_length=300)

class ExpenseUpdate(BaseModel):
    title:Optional[str]=Field(None,min_length=2,max_length=100)
    amount:Optional[float]=Field(None,gt=0)
    category:Optional[str]=Field(None,min_length=2,max_length=30)
    description:Optional[str]=Field(None,max_length=300)

class Expense(ExpenseCreate):
    id:int
