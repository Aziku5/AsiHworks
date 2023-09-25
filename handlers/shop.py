import db.queries
from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from db.queries import get_product

shop_router = Router()


@shop_router.message(Command("shop"))
async def shop(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text="ЛИСТ А4"),
            KeyboardButton(text="КИСТЬ"),
            KeyboardButton(text="КАРТИНКА")
        ]]
    )
    await message.answer("Выберите категорию ниже:", reply_markup=kb)


@shop_router.message(F.text == "ЛИСТ А4")
async def show_list(message: types.Message):
    await message.answer(get_product()[0][1])


@shop_router.message(F.text == "КИСТЬ")
async def show_kist(message: types.Message):
    await message.answer(get_product()[1][1])


@shop_router.message(F.text == "КАРТИНКА")
async def show_kartina(message: types.Message):
    await message.answer(get_product()[2][1])