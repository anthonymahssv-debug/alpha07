# Santa Fe CI API Hotfix Bundle

This bundle is the fastest workaround to stop the product from being static-only.

It includes:

- Canonical frontend files in `frontend/`
- Real backend API in `backend/`
- SQLite seed/database layer
- Alert engine
- Score normalization/fallback engine
- System health endpoint
- Static `data.json` fallback retained as demo/offline data

## Run locally

```bash
cd santa-fe-ci-api-hotfix
python3 -m venv .venv && source .venv/bin/activate && pip install -r backend/requirements.txt && python -m backend.seed && uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
```

Then open:

```text
http://127.0.0.1:8000
```

Test API:

```text
http://127.0.0.1:8000/api/health
http://127.0.0.1:8000/api/system/health
http://127.0.0.1:8000/api/feed
http://127.0.0.1:8000/api/alerts
http://127.0.0.1:8000/api/openapi.json
```

## Important honesty rule

This API is real, but the current data source is seeded from `frontend/data.json`.
Until an external collector/source integration is added, the health endpoint labels this as demo/static-seeded data rather than pretending it is fresh external live data.
