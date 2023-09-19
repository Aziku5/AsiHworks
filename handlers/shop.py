from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove

shop_router = Router()


@shop_router.message(Command("shop"))
async def shop(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text="Раскраски"),
            KeyboardButton(text="Комиксы"),
            KeyboardButton(text="Книги")
        ]]
    )
    await message.answer("Выберите категорию ниже:", reply_markup=kb)


@shop_router.message(F.text == "Раскраски")
async def show_manga(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("Виды раскраски в нашем магазине:", reply_markup=kb)


@shop_router.message(F.text == "Комиксы")
async def show_manga(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("Список комиксов в нашем магазине:", reply_markup=kb)


@shop_router.message(F.text == "Книги")
async def show_manga(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("Список книг в нашем магазине:", reply_markup=kb)