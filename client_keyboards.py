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
# divisions menu buttons
btn_1 = KeyboardButton(text='УПЗ')
btn_2 = KeyboardButton(text='В.Бистра')
btn_3 = KeyboardButton(text='Стужиця')
btn_4 = KeyboardButton(text='Княгиня')
btn_5 = KeyboardButton(text='В.Березний')
btn_6 = KeyboardButton(text='Новоселиця')
btn_7 = KeyboardButton(text='Камяниця')
btn_8 = KeyboardButton(text='Гута')
btn_9 = KeyboardButton(text='Оноківці')
btn_10 = KeyboardButton(text='Ужгород')
btn_11 = KeyboardButton(text='П.Комарівці')
btn_12 = KeyboardButton(text='Соломонове')
btn_13 = KeyboardButton(text='Саловка')
btn_14 = KeyboardButton(text='НМК"Вогник"')

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
# menu divisions constr
div_keyboard = ReplyKeyboardMarkup(keyboard=[
    [btn_1, btn_2, btn_3],
    [btn_4, btn_5, btn_6],
    [btn_7, btn_8, btn_9],
    [btn_10, btn_11, btn_12],
    [btn_13, btn_14]
], resize_keyboard=True)
