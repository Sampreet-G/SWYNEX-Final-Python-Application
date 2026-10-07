# SWYNEX Final Python Application

A production-style **Expense Tracker REST API** built with FastAPI for Task 4 of the SWYNEX Technologies Python Developer Internship.

## Features
- CRUD expense management
- Expense total summary
- Health-check endpoint
- JSON persistence
- Pydantic validation
- HTTP error handling
- Swagger documentation
- Automated pytest tests
- Modular project structure

## Structure
```text
SWYNEX-Final-Python-Application/
├── app/
│   ├── main.py
│   ├── models.py
│   └── database.py
├── data/expenses.json
├── tests/test_api.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Setup
```bash
python -m venv venv
```
Windows:
```bash
venv\Scripts\activate
```
Install:
```bash
pip install -r requirements.txt
```

## Run
```bash
uvicorn app.main:app --reload
```
Open `http://127.0.0.1:8000/docs` for Swagger UI.

## Endpoints
- GET `/`
- GET `/health`
- GET `/expenses`
- GET `/expenses/{id}`
- POST `/expenses`
- PUT `/expenses/{id}`
- DELETE `/expenses/{id}`
- GET `/expenses/summary/total`

## Example POST
```json
{"title":"Python Course","amount":1200,"category":"Education","description":"Online course"}
```

## Testing
```bash
pytest
```

The API validates required fields, string lengths and positive amounts, and returns 404 when an expense does not exist.

## Internship Task
**Task 4: Final Python Application**
