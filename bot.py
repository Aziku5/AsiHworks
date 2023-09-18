from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher

load_dotenv()
token = getenv("BOT_TOKEN")
bot = Bot(token=token)
dp = Dispatcher()
