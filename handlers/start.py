from aiogram.filters import Command
from aiogram import types, Router, F
from texts import START_TEXT
from texts import ABOUT_US
import random
import os
from aiogram.types.inline_keyboard_button import InlineKeyboardButton as IButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from bot import bot

start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                IButton(text="Наш инстаграм", url="https://instagram.com"),
                IButton(text="Наш aдрес", callback_data="ЦУМ"),
            ],
            [
                IButton(text="О нас", callback_data="ABOUT_US")
            ]
        ]
    )
    await message.answer(START_TEXT, reply_markup=kb)


@start_router.callback_query(F.data == "ABOUT_US")
async def about(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.message.chat.id,
                           text=ABOUT_US)


@start_router.message(Command("photo"))
async def send_random_picture(message: types.Message):
    images_folder = "images/"
    images = [f for f in os.listdir(images_folder) if f.endswith((".jpg", ".jpeg", ".png"))]
    if images:
        random_image = random.choice(images)
        file = types.FSInputFile(images_folder + random_image)
        await message.answer_photo(file)
    else:
        await message.answer("В папке с картинками нет подходящих файлов.")


@start_router.message(Command("myinfo"))
async def my_info(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username

    info_message = f"Ваш ID: {user_id}\nИмя: {first_name}\nUsername: @{username}"
    await message.answer(info_message)
