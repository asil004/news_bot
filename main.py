import asyncio
import logging
import os
import sys
from aiogram import Dispatcher, Router, Bot, types
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from routers import router as all_routers
from aiohttp import BasicAuth
from aiogram.client.session.aiohttp import AiohttpSession

load_dotenv('.env')

# auth = BasicAuth(login="HFPFKY", password="Nd7nsR")
# session = AiohttpSession(proxy=("protocol://45.145.57.236:10411", auth))

bot = Bot(token=os.getenv('BOT_TOKEN'), parse_mode=ParseMode.HTML)

router = Router()
router.include_router(all_routers)


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):
        logging.info('Bot stopped')
