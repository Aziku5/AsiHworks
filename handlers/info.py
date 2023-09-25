from aiogram import types, Router
from aiogram.filters import Command

info_router = Router()


@info_router.message(Command("myinfo"))
async def info(message: types.Message):
    print(message.from_user)
    await message.answer(
        f"Ваш id: {message.from_user.id}, Ваш first_name: {message.from_user.first_name}, "
        f"Ваш username: {message.from_user.username}",
    )
