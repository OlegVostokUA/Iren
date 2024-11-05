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
# divisions menu buttons
btn_1 = KeyboardButton(text='УПЗ.')
btn_2 = KeyboardButton(text='В.Бистра.')
btn_3 = KeyboardButton(text='Стужиця.')
btn_4 = KeyboardButton(text='Княгиня.')
btn_5 = KeyboardButton(text='В.Березний.')
btn_6 = KeyboardButton(text='Новоселиця.')
btn_7 = KeyboardButton(text='Камяниця.')
btn_8 = KeyboardButton(text='Гута.')
btn_9 = KeyboardButton(text='Оноківці.')
btn_10 = KeyboardButton(text='Ужгород.')
btn_11 = KeyboardButton(text='П.Комарівці.')
btn_12 = KeyboardButton(text='Соломонове.')
btn_13 = KeyboardButton(text='Саловка.')
btn_14 = KeyboardButton(text='НМК"Вогник".')


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
# food_intake_menu_admin = ReplyKeyboardMarkup(keyboard=[
#     [btn_breakfast, btn_dinner, btn_supper],
#     [btn_mark_month, button_back]
# ], resize_keyboard=True)

# menu divisions constr
div_keyboard_admin = ReplyKeyboardMarkup(keyboard=[
    [btn_1, btn_2, btn_3],
    [btn_4, btn_5, btn_6],
    [btn_7, btn_8, btn_9],
    [btn_10, btn_11, btn_12],
    [btn_13, btn_14],
    [btn_mark_month, button_back]
], resize_keyboard=True)
