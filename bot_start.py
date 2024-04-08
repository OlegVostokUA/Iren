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
from keyboards import main_keyboard, task_keyboard
from google.google_functions import func_parce_foul, func_parce_short

from config import TOKEN


storage = MemoryStorage()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=storage)


@dp.message(CommandStart())
async def command_start(message: Message):
    await message.answer(f'Hello, {message.from_user.full_name}', reply_markup=main_keyboard)


@dp.message(Command('<Back'))
async def back_func(message: Message):
    await message.answer('Ok', reply_markup=main_keyboard)


@dp.message(Command('Tasks'))
async def tasks_func(message: Message):
    await message.answer('Tasks parse menu', reply_markup=task_keyboard)


@dp.message(Command('Foul_tasks'))
async def foul_tasks_func(message: Message):
    text = func_parce_foul()
    await message.answer(text, reply_markup=task_keyboard)


@dp.message(Command('Short_tasks'))
async def short_tasks_func(message: Message):
    text = func_parce_short()
    await message.answer(text, reply_markup=task_keyboard)


# func for start bot
async def main():
    print('BOT online')
    #start_database()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
