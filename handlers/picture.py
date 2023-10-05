from aiogram import types, Router
from aiogram.filters import Command
import random


picture_router = Router()


@picture_router.message(Command("picture"))
async def send_random_photo(message: types.Message):
    file = types.FSInputFile("images/Baby yoda.jpg")
    file2 = types.FSInputFile("images/F2.jpg")
    file3 = types.FSInputFile("images/fred-852770.jpg")
    file4 = types.FSInputFile("images/shutterstock_88734232.jpg")
    file5 = file, file2, file3, file4
    random_photo = random.choice(file5)
    await message.answer_photo(random_photo)
