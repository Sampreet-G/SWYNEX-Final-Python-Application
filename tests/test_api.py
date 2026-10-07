from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)

def test_health():
    r=client.get("/health"); assert r.status_code==200; assert r.json()["status"]=="healthy"

def test_create_expense():
    r=client.post("/expenses",json={"title":"Test Expense","amount":100,"category":"Education","description":"Test"})
    assert r.status_code==201 and r.json()["title"]=="Test Expense"

def test_missing_expense():
    assert client.get("/expenses/999999").status_code==404
