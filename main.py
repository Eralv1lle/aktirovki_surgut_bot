from aiogram import Bot, Dispatcher

import asyncio
import logging

from config import config
from app.handlers import routers
from app.scheduler import setup_scheduler


bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()
dp.include_routers(*routers)


async def main():
    setup_scheduler(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен пользователем")
    except Exception as err:
        print(f"Упал: {err}")