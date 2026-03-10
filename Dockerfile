# Базовый образ
FROM python:3.10-slim

# Установим рабочую директорию
WORKDIR /app

# Установим переменные окружения
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Обновим пакеты и установим зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Копируем зависимости и устанавливаем их
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальную часть приложения
COPY . .

# Создаем и даем права на директорию для статических файлов
RUN mkdir -p /app/staticfiles && chmod -R 755 /app/staticfiles

# Прокидываем порт Django
EXPOSE 8000

# Меняем пользователя для безопасности
USER www-data

# Запускаем приложение
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:8000"]
