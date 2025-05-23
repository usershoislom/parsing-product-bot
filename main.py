import asyncio

from aiogram import Bot, Dispatcher

from config.config import BOT_TOKEN
from config.logger import logger
from handlers import user_handlers


async def main():
    logger.info("Starting bot")
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(user_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
