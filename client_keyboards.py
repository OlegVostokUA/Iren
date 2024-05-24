from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# main menu buttons
button_help = KeyboardButton(text='/Допомога')
button_rating = KeyboardButton(text='/Оцінити')
# food intake menu buttons
btn_breakfast = KeyboardButton(text='Сніданок')
btn_dinner = KeyboardButton(text='Обід')
btn_supper = KeyboardButton(text='Вечеря')
# food marks menu buttons
btn_five = KeyboardButton(text='5')
btn_four = KeyboardButton(text='4')
btn_three = KeyboardButton(text='3')
btn_two = KeyboardButton(text='2')
btn_one = KeyboardButton(text='1')

# main menu constr
main_keyboard_cl = ReplyKeyboardMarkup(keyboard=[
    [button_help, button_rating]
], resize_keyboard=True)
# food intake menu
food_intake_menu = ReplyKeyboardMarkup(keyboard=[
    [btn_breakfast, btn_dinner, btn_supper]
], resize_keyboard=True)
# food marks menu
food_marks_menu = ReplyKeyboardMarkup(keyboard=[
    [btn_five, btn_four, btn_three],
    [btn_two, btn_one]
], resize_keyboard=True)
