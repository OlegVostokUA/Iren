from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#main menu buttons
button_tasks = KeyboardButton(text='/Tasks')

# task menu buttons
button_task_foul = KeyboardButton(text='/Foul_tasks')
button_task_short = KeyboardButton(text='/Short_tasks')


button_back = KeyboardButton(text='/<Back')

# main menu constr
main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [button_tasks]
], resize_keyboard=True)

# tasks menu constr
task_keyboard = ReplyKeyboardMarkup(keyboard=[
    [button_task_foul, button_task_short],
    [button_back]
], resize_keyboard=True)