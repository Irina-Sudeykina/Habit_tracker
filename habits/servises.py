import os

import requests
from dotenv import load_dotenv

load_dotenv(override=True)


def send_telegram_message(chat_id, message):
    # Токен бота и HTTP-запрос
    bot_token = os.getenv("TG_BOT")
    tg_url = os.getenv("TG_URL")

    url = f"{tg_url}bot{bot_token}/sendMessage"

    # Параметры запроса
    params = {"chat_id": chat_id, "text": message}

    response = requests.get(url, params=params)

    # Обработка ответа сервера
    if response.status_code == 200:
        json_data = response.json()
        print("Ответ API:", json_data)
    else:
        print(f"Ошибка: {response.status_code}")
