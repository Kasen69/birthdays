# config.py
import os
from dotenv import load_dotenv

# Завантажуємо локальний .env файл (якщо запускаєте на комп'ютері)
load_dotenv()

# Отримуємо токен з безпечних змінних середовища
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ Помилка: Не знайдено BOT_TOKEN у змінних середовища!")