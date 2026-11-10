# config.py
import os

# Отримуємо токен напряму зі змінних середовища хостингу
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ Помилка: Не знайдено BOT_TOKEN у змінних середовища!")