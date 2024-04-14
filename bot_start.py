import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import requests
from keyboards import main_keyboard, task_keyboard, parse_keyboard
from google.google_functions import func_parce_foul, func_parce_short, func_parse_central
from parsing.parsing_functions import parse_prices

from config import TOKEN


storage = MemoryStorage()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=storage)

centraliz = None


@dp.message(CommandStart())
async def command_start(message: Message):
    await message.answer(f'Hello, {message.from_user.full_name}', reply_markup=main_keyboard)


@dp.message(Command('<Back'))
async def back_func(message: Message):
    await message.answer('Ok', reply_markup=main_keyboard)


# tasks functions block
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


# parser functions block
@dp.message(Command('Parsers'))
async def tasks_func(message: Message):
    await message.answer('Tasks parse menu', reply_markup=parse_keyboard)


@dp.message(Command('Prices'))
async def foul_tasks_func(message: Message):
    text_for_msg = parse_prices()
    await message.answer(text_for_msg, reply_markup=parse_keyboard)


# central parse functions block
@dp.message(Command('Central'))
async def parse_central(message: Message):
    global centraliz
    centr_list = func_parse_central()
    centraliz = centr_list
    for i in centr_list:
        await message.answer(f'{i[3]}-{i[4]}')
        builder_inline = InlineKeyboardBuilder()
        builder_inline.add(InlineKeyboardButton(text='Choice', callback_data=f'choice {i[3]} {i[4]}'))
        await message.answer('^^^', reply_markup=builder_inline.as_markup())


@dp.callback_query(F.data.startswith('choice'))
async def choice_central(callback: types.CallbackQuery):
    query = callback.data[7:]
    query = query.rsplit(' ', 1)
    for i in centraliz:
        if query[0] in i and query[1] in i:
            text = i
    text_for_msg = f'1493\nВідповідно до розп. АДПСУ №{text[0]} від {text[1]} отримано від {text[2]} {text[3]} - {text[4]}.\nЯкість відповідає вимогам.'
    await callback.message.answer(text_for_msg)

# choice Сало шпик 700
# [['06.1.2/15817-24', '11.03.2024', 'ГЦКБРтаЗ', 'Дієтична добавка Гексавіт', '50000'], ['06.1.2/13354-24', '29.02.202 .......
# func for start bot
async def main():
    print('BOT online')
    #start_database()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
