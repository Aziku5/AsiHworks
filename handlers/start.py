from aiogram.filters import Command
from aiogram import types, Router, F
from aiogram.types.inline_keyboard_button import InlineKeyboardButton as IButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from texts import START_TEXT
from texts2 import BUTTON_TEXT

start_router = Router()


@start_router.message(Command("start"))
async def hello(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                IButton(text="Контакты", callback_data="contacts"),
                IButton(text="О нас", callback_data="about"),
                IButton(text="Наш сайт", url="https://google.com"),
            ]
        ]
    )
    await message.answer(START_TEXT, reply_markup=kb)


@start_router.callback_query(F.data == "ABOUT_US")
async def about(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer(BUTTON_TEXT)


@start_router.callback_query(F.data == "contacts")
async def about(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer("911")
