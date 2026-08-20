FROM python:3.11-slim

WORKDIR /app

# Копируем зависимости и исходный код
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server_FASTAPI.py .
COPY base.db .

# Запускаем Uvicorn сервер
CMD ["uvicorn", "server_FASTAPI:app", "--host", "0.0.0.0", "--port", "8000"]