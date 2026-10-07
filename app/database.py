import json,os
from app.models import ExpenseCreate,ExpenseUpdate
DATA_FILE="data/expenses.json"

class ExpenseDatabase:
    def __init__(self): self.expenses=self._load()
    def _load(self):
        os.makedirs("data",exist_ok=True)
        if not os.path.exists(DATA_FILE): return []
        try:
            with open(DATA_FILE,encoding="utf-8") as f: return json.load(f)
        except (json.JSONDecodeError,OSError): return []
    def _save(self):
        os.makedirs("data",exist_ok=True)
        with open(DATA_FILE,"w",encoding="utf-8") as f: json.dump(self.expenses,f,indent=4)
    def get_all(self): return self.expenses
    def get(self,i): return next((x for x in self.expenses if x["id"]==i),None)
    def create(self,e:ExpenseCreate):
        item={"id":max((x["id"] for x in self.expenses),default=0)+1,**e.model_dump()}
        self.expenses.append(item); self._save(); return item
    def update(self,i,e:ExpenseUpdate):
        item=self.get(i)
        if not item:return None
        item.update(e.model_dump(exclude_unset=True)); self._save(); return item
    def delete(self,i):
        item=self.get(i)
        if not item:return False
        self.expenses.remove(item); self._save(); return True
    def total_amount(self): return round(sum(x["amount"] for x in self.expenses),2)
