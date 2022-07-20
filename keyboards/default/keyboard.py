from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

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

location = InlineKeyboardMarkup(row_width=2)
location.add(InlineKeyboardButton(text='Hashtag 1.0', callback_data='hashtag_1_0'),
             InlineKeyboardButton(text='Hashtag 2.0', callback_data='hashtag_2_0'),
             InlineKeyboardButton(text='Літній майданчик 1.0', callback_data='litniy_maydanchik_1_0'),
             InlineKeyboardButton(text='Літній майданчик 2.0', callback_data='litniy_maydanchik_2_0'),
             )
