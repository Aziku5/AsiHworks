from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from db.queries import get_product_by_category

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
    listy = get_product_by_category(1)
    kb = ReplyKeyboardRemove()
    await message.answer("Список листов:", reply_markup=kb)
    for f in listy:
        await message.answer(f[1])


@shop_router.message(F.text == "КИСТЬ")
async def show_kist(message: types.Message):
    kisty = get_product_by_category(2)
    kb = ReplyKeyboardRemove()
    await message.answer("Список кисть:", reply_markup=kb)
    for y in kisty:
        await message.answer(y[1])


@shop_router.message(F.text == "КАРТИНКА")
async def show_kartina(message: types.Message):
    kartink = get_product_by_category(3)
    kb = ReplyKeyboardRemove()
    await message.answer("Список картин:", reply_markup=kb)
    for o in kartink:
        await message.answer(o[1])
