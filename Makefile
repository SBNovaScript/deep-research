.PHONY: backend frontend

backend:
	cd backend && uvicorn app.main:app --reload

frontend:
	cd frontend && npm run dev
