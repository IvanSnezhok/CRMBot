from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

remove_keyboard = ReplyKeyboardRemove()
auth_contact = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Відправити контакт', request_contact=True)
    ]
], resize_keyboard=True, one_time_keyboard=True)

main_menu = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Зміна')
    ],
    [
        KeyboardButton(text='Чек-листи')
    ],
    [
        KeyboardButton(text='Мої гроші')
    ],
    [
        KeyboardButton(text='База знань')
    ],
], resize_keyboard=True, one_time_keyboard=True)

geo_send = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Відправити гео-локацію', request_location=True)
    ]
], resize_keyboard=True, one_time_keyboard=True)

add_money = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Додати гроші'),
        KeyboardButton(text='Назад')
    ]
], resize_keyboard=True, one_time_keyboard=True)


