import asyncio
import logging
from aiogram import Dispatcher
from bot_instance import bot
from handlers import mainbot
logging.basicConfig(level=logging.INFO,
                    format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
                    )

async def main():
    dp = Dispatcher()

    dp.include_routers(
        mainbot.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    print('запущен')
    asyncio.run(main())