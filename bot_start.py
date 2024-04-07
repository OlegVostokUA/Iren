import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, FSInputFile
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import requests

from config import TOKEN


storage = MemoryStorage()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=storage)


@dp.message(CommandStart())
async def command_start(message: Message):
    await message.answer(f'Hello, {message.from_user.full_name}')


# func for start bot
async def main():
    print('BOT online')
    #start_database()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
