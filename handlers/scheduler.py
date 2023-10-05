from aiogram import types, Router
from aiogram.filters import Command
from bot import scheduler, bot
from db.queries import select_sub

scheduler_router=Router()

@scheduler_router.message(Command("sub"))
async def remide_me():
    for user_id in select_sub():
        scheduler.add_job(
            send_remide,
            "interval",
            seconds=5,
            args=user_id
        )




async def send_remide(user_id:int):
    await bot.send_message(str(user_id), 'Hello')