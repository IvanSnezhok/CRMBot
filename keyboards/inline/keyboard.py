from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

location = InlineKeyboardMarkup(row_width=2)
location.add(InlineKeyboardButton(text='Hashtag 1.0', callback_data='hashtag_1_0'),
             InlineKeyboardButton(text='Hashtag 2.0', callback_data='hashtag_2_0'),
             InlineKeyboardButton(text='Літній майданчик 1.0', callback_data='litniy_maydanchik_1_0'),
             InlineKeyboardButton(text='Літній майданчик 2.0', callback_data='litniy_maydanchik_2_0')
             )

check_lists_read = InlineKeyboardMarkup(row_width=2)
check_lists_read.add(InlineKeyboardButton(text='Чек-лист 1.0', callback_data='check_list_1_0'),
                    InlineKeyboardButton(text='Чек-лист 2.0', callback_data='check_list_2_0'),
                    InlineKeyboardButton(text='Літній майданчик 1.0', callback_data='litniy_maydanchik_1_0'),
                    InlineKeyboardButton(text='Літній майданчик 2.0', callback_data='litniy_maydanchik_2_0'))

check_list1 = InlineKeyboardMarkup(row_width=1)

check_list2 = InlineKeyboardMarkup(row_width=1)

outside_list = InlineKeyboardMarkup(row_width=1)

outside_list2 = InlineKeyboardMarkup(row_width=1)

