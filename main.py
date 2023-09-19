import asyncio
import logging
from bot import bot, dp
from handlers import (
    start_router,
    shop_router,
    echo_router
)


async def main():
    dp.include_router(start_router)
    dp.include_router(shop_router)
    dp.include_router(echo_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
