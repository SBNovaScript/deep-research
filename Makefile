.PHONY: backend frontend

backend:
	cd backend && export UV_ENV_FILE=.env && uv run uvicorn app.main:app --reload

frontend:
	cd frontend && npm run dev
