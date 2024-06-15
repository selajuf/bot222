import os
from aiogram import Router
from aiogram.filters import CommandStart
from db import Database
from bot_instance import bot
from dotenv import load_dotenv, find_dotenv
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton


router = Router()

db = Database('db.db')

load_dotenv(find_dotenv())

bot_nick = os.getenv("BOT_NICK")

main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Профиль")],
    ],
    resize_keyboard=True
)

@router.message(CommandStart())
async def start(message: Message):
    if not db.user_exists(message.from_user.id):
        start_command = message.text
        referrer_id = str(start_command[7:])
        if str(referrer_id) != "":
            if str(referrer_id) != str(message.from_user.id):
                db.add_user(message.from_user.id, referrer_id)
                try:
                    await bot.send_message(chat_id=referrer_id, text='Кто то перешел по твоей ссылке')
                except Exception as e:
                    print(f"{e}")
            else:
                db.add_user(message.chat.id)
                await message.answer("Нельзя зарегаться по своей ссылке")
        else:
            db.add_user(message.chat.id)

    await message.answer("Привет!", reply_markup=main_menu_keyboard)

@router.message()
async def bot_message(message: Message):
    if message.chat.type == 'private':
        if message.text == "Профиль":
            referrals_count = db.count_referrals(message.from_user.id)
            await bot.send_message(message.from_user.id, f"ID: {message.from_user.id}\nt.me/{bot_nick}?start={message.from_user.id}\nКоличество рефералов: {referrals_count}")
