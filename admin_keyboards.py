from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# main menu buttons
button_tasks = KeyboardButton(text='/Tasks')
button_parse = KeyboardButton(text='/Parsers')
button_central = KeyboardButton(text='/Central')
button_food_marks = KeyboardButton(text='/Food_marks')
# task menu buttons
button_task_foul = KeyboardButton(text='/Foul_tasks')
button_task_short = KeyboardButton(text='/Short_tasks')
# parsing menu buttons
button_prices_parse = KeyboardButton(text='/Prices')
# food intake menu buttons
btn_breakfast = KeyboardButton(text='Сніданок.')
btn_dinner = KeyboardButton(text='Обід.')
btn_supper = KeyboardButton(text='Вечеря.')
btn_mark_month = KeyboardButton(text='/Marks_for_month')


button_back = KeyboardButton(text='/<Back')

# main menu constr
main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [button_tasks, button_parse, button_central],
    [button_food_marks] #
], resize_keyboard=True)

# tasks menu constr
task_keyboard = ReplyKeyboardMarkup(keyboard=[
    [button_task_foul, button_task_short],
    [button_back]
], resize_keyboard=True)

# parsing menu constr
parse_keyboard = ReplyKeyboardMarkup(keyboard=[
    [button_prices_parse],
    [button_back]
], resize_keyboard=True)
# food intake menu
food_intake_menu_admin = ReplyKeyboardMarkup(keyboard=[
    [btn_breakfast, btn_dinner, btn_supper],
    [btn_mark_month, button_back]
], resize_keyboard=True)
