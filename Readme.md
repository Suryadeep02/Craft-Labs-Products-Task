# Craft Labs – Product API

## Backend
```bash
cd Backend
uvicorn main:app --reload
```

API runs at `http://localhost:8000`  
Docs at `http://localhost:8000/docs`

---

## Frontend
```bash
cd craft-labs-ui
npm install
npm run dev
```

App runs at `http://localhost:5173`

---

## Running Tests
```bash
cd Backend
pytest tests/ -v
```