import asyncio
import logging
import sys
from datetime import datetime

from aiogram import Bot, Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import requests
from admin_keyboards import main_keyboard, task_keyboard, parse_keyboard, food_intake_menu_admin
from client_keyboards import main_keyboard_cl, food_intake_menu, food_marks_menu
from google.google_functions import func_parce_foul, func_parce_short, func_parse_central
from parsing.parsing_functions import parse_prices
from database.sq_lite_db import sql_start, add_to_db, read_db, select_marks

from config import TOKEN


storage = MemoryStorage()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=storage)

centraliz = None
ADMIN_ID = 1064924678


# finite state machine class
class FSMClientFoodRating(StatesGroup):
    food_intake = State()
    mark = State()


@dp.message(CommandStart())
async def command_start(message: Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer(f'Hello, {message.from_user.full_name}', reply_markup=main_keyboard)
    else:
        await message.answer(f'Доброго дня, {message.from_user.full_name}!\n'
                             f'Щоб дізнатись що вміє цей бот - \n'
                             f'скористайтеся клавішею \n"/Допомога"', reply_markup=main_keyboard_cl)


@dp.message(Command('<Back'))
async def back_func(message: Message):
    await message.answer('Ok', reply_markup=main_keyboard)


# # # ADMIN FUNCTIONS # # #
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


@dp.message(Command('Food_marks'))
async def marks_keyboard_func(message: Message):
    await message.answer('Ok', reply_markup=food_intake_menu_admin)


@dp.message(F.text == 'Сніданок.')
@dp.message(F.text == 'Обід.')
@dp.message(F.text == 'Вечеря.')
async def marks_parse_func(message: Message):
    food_intake = message.text[:-1]
    data = read_db(food_intake)
    marks = []
    count = 0
    sum = 0
    for i in data:
        msg_line = f'{i[3]} - {i[2]}\n'
        marks.append(msg_line)
        if i[2] not in [1,2,3,4,5]:
            continue
        else:
            count += 1
            sum = sum + i[2]
    try:
        middle_mark = round(sum / count, 1)
    except:
        middle_mark = 0
    marks.append(f'\nСередній бал: {middle_mark}')
    text_for_msg = ''.join(marks)
    await message.answer(text_for_msg, reply_markup=food_intake_menu_admin)


@dp.message(Command('Marks_for_month'))
async def middle_marks(message: Message):
    data = select_marks()
    date = data[0][0]
    string_of_marks = ''
    count = 0
    mark = 0
    for i in data:
        if date == i[0]:
            count += 1
            mark += i[1]
        else:
            midle_mark = str(round(mark / count, 2))
            string_of_marks + date + ': ' + midle_mark + '\n'
            date = i[0]
            count = 1
            mark = 0
            mark += i[1]
    midle_mark = str(round(mark / count, 2))
    string_of_marks += date + ': ' + midle_mark + '\n'
    await message.answer(string_of_marks, reply_markup=food_intake_menu_admin)


# # # CLIENT FUNCTIONS # # #
@dp.message(Command('Допомога'))
async def help_client(message: Message):
    await message.answer('Цей бот створено з метою\n'
                         'оцінки якості харчування\n'
                         '\n'
                         'Для того щоб надати оцінку\n'
                         'натисніть клавішу "/Оцінити"\n', reply_markup=main_keyboard_cl)


@dp.message(Command('Оцінити'))
async def rated_food_start(message: Message, state: FSMContext):
    await state.set_state(FSMClientFoodRating.food_intake)
    await message.answer('Оберіть прийом їжі, який хотіли би оцінити', reply_markup=food_intake_menu)


@dp.message(FSMClientFoodRating.food_intake)
async def food_intake_load(message: Message, state: FSMContext):
    await state.update_data(food_intake=message.text)
    await state.set_state(FSMClientFoodRating.mark)
    await message.answer('Оцініть прийом їжі від 1 до 5 за допомогою представлених клавіш', reply_markup=food_marks_menu)


@dp.message(FSMClientFoodRating.mark)
async def mark_load(message: Message, state: FSMContext):
    try:
        await state.update_data(mark=int(message.text))
    except:
        await state.update_data(mark=0)
    data = await state.get_data()
    try:
        name_tg = (message.from_user.full_name,)
    except:
        name_tg = ('UNKNOWN',)
    data = (datetime.today().strftime("%d.%m.%Y"),) + tuple(data.values()) + name_tg
    add_to_db(data)
    await state.clear()
    await message.answer('Дякуємо за вашу оцінку.\nЦе дуже важливо для нас', reply_markup=main_keyboard_cl)


@dp.message()
async def echo_send(message: types.Message):
    await message.answer('Вибачте, я Вас не розумію', reply_markup=main_keyboard_cl)


# # # MAIN BLOCK # # #
async def main():
    print('BOT online')
    sql_start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
