FROM python:3.11-slim

WORKDIR /app

# Встановлюємо залежності
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код
COPY app/ ./app/
COPY app/templates/ ./app/templates/

# Виставляємо робочу директорію
WORKDIR /app/app

# Відкриваємо порт
EXPOSE 80

# Healthcheck
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost/health || exit 1

# Запускаємо додаток
CMD ["python", "main.py"]
