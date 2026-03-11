# FastAPI OpenAPI Items Starter

Yksinkertainen mutta laajennettava FastAPI-projekti, jossa OpenAPI-dokumentaatio generoituu automaattisesti FastAPI:n vakio-ominaisuuksilla.

## Hakemistorakenne

```text
fastapi-openapi-items/
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── health.py
│   │   │   └── items.py
│   │   └── router.py
│   ├── core/
│   │   └── config.py
│   ├── models/
│   │   └── item.py
│   ├── services/
│   │   └── items_service.py
│   └── main.py
├── plantuml/
│   └── architecture.mmd
├── tests/
│   ├── conftest.py
│   └── test_api.py
├── .env.example
├── .gitignore
├── Dockerfile
├── pyproject.toml
├── README.md
└── requirements.md
```

## Paikallinen käynnistys

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev]
uvicorn app.main:app --reload --port 8000
```

## Testien ajo

```bash
pytest
```

## Linttaus

```bash
ruff check .
```

## Tyyppitarkistus

```bash
mypy app tests
```

## Docker-käynnistys

```bash
docker build -t fastapi-openapi-items .
docker run --rm -p 8000:8000 fastapi-openapi-items
```

## OpenAPI URLit

- OpenAPI JSON: `http://localhost:8000/openapi.json`
- Swagger UI (Docs): `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Arkkitehtuurikaavio

- Mermaid-lähde: `plantuml/architecture.mmd`

GitHub renderöi Mermaidin suoraan markdownissa. Halutessasi voit renderöidä PNG:n lokaalisti Mermaid CLI:llä:

```bash
mmdc -i plantuml/architecture.mmd -o plantuml/architecture.png
```

## API endpointit

- `GET /api/health`
- `GET /api/items`
- `POST /api/items`
- `GET /api/items/{item_id}`
