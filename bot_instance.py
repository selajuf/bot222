import os
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

load_dotenv(find_dotenv())

telegram_token = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=telegram_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))