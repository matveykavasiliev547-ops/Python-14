FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir fastapi uvicorn pydantic psycopg2-binary sqlalchemy

COPY . .

CMD ["uvicorn", "GJ_API_SERVER:app", "--host", "0.0.0.0", "--port", "8000"]