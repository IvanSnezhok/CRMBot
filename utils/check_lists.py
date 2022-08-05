import csv
import operator
import pathlib

from typing import Dict

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.kbd import Multiselect, Button, Group, Column
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.when import Whenable

from data.gsheet import update_all
from loader import db, dp, registry

from states.diaolg_states import  CheckList1, CheckList2, LitniyMaydanchik1, LitniyMaydanchik2


def csv_to_list_of_tuple_text(csv_io):
    with open(csv_io, 'r') as f:
        reader = csv.reader(f)
        temp = []
        result = []
        for row in reader:
            temp.append(row[0])
        temp.remove('Text')
        for x, y in enumerate(temp):
            result.append((y, x))
        return result


# async def multiselect_items():
# result = {
#     "hashtag_1_0": False,
#     "hashtag_2_0": False,
#     "litniy_maydanchik_1_0": False,
#     "litniy_maydanchik_2_0": False,
#     "close_lists_1_0": False,
#     "close_lists_2_0": False,
#     "close_maydanchik_1_0": False,
#     "close_maydanchik_2_0": False,
# }
# if key == 'hashtag_1_0':
#     result['hashtag_1_0'] = True
# elif key == 'hashtag_2_0':
#     result['hashtag_2_0'] = True
# elif key == 'litniy_maydanchik_1_0':
#     result['litniy_maydanchik_1_0'] = True
# elif key == 'litniy_maydanchik_2_0':
#     result['litniy_maydanchik_2_0'] = True
# elif key == 'close_lists_1_0':
#     result['close_lists_1_0'] = True
# elif key == 'close_lists_2_0':
#     result['close_lists_2_0'] = True
# elif key == 'close_maydanchik_1_0':
#     result['close_maydanchik_1_0'] = True
# elif key == 'close_maydanchik_2_0':
#     result['close_maydanchik_2_0'] = True
# return result


def multiselect(items):
    buttons = Multiselect(
        checked_text=Format('✓ {item[0]}'),
        unchecked_text=Format('✖ {item[0]}'),
        id='multiselect',
        item_id_getter=operator.itemgetter(1),
        items=items,
    )
    return buttons


#
# dialog = Dialog(
#     Window(
#         Format("Чек-лист"),
#         Group(
#             Column(multiselect(csv_to_list_of_tuple_text('check_list_1_0.csv')), when="hashtag_1_0"),
#             Column(multiselect(csv_to_list_of_tuple_text('check_list_2_0.csv')), when="hashtag_2_0"),
#             Column(multiselect(csv_to_list_of_tuple_text('litniy_maydanchik_1_0.csv')), when="litniy_maydanchik_1_0"),
#             Column(multiselect(csv_to_list_of_tuple_text('litniy_maydanchik_2_0.csv')), when="litniy_maydanchik_2_0"),
#             Column(multiselect(csv_to_list_of_tuple_text('close_check_list_1_0.csv')), when="close_lists_1_0"),
#             Column(multiselect(csv_to_list_of_tuple_text('close_check_list_2_0.csv')), when="close_lists_2_0"),
#             Column(multiselect(csv_to_list_of_tuple_text('close_litniy_maydanchik_1_0.csv')), when="close_maydanchik_1_0"),
#             Column(multiselect(csv_to_list_of_tuple_text('close_litniy_maydanchik_2_0.csv')), when="close_maydanchik_2_0"),
#             Button("Закриття зміни", id='close'),
#             Button('Технічна перерва', id='technical_break')
#         ), state=DialogStates.cl1, getter=multiselect_items
#     )
# )

#
#
#
async def dialogs_manager(key: str):
    update_all(key)
    dialog1 = Dialog(
        Window(
            Const("Ваш Чек-лист 1.0"),
            Group(
                Column(multiselect(csv_to_list_of_tuple_text("check_list_1_0.csv"))),
                Button(Const('Закриття зміни'), id='close', on_click=close_shift),
                Button(Const('Технічна перерва'), id='break')), state=CheckList1.cl1),
        Window(
            Const("Закриття зміни, Хештег 1.0"),
            Group(
                Column(multiselect(csv_to_list_of_tuple_text("close_check_list_1_0.csv"))),
                Button(Const('Технічна перерва'), id='break')), state=CheckList1.ccl1))


    dialog2 = Dialog(
        Window(
            Const("Ваш Чек-лист 2.0"),
            Group(
                Column(multiselect(csv_to_list_of_tuple_text("check_list_2_0.csv"))),
                Button(Const('Закриття зміни'), id='close', on_click=close_shift),
                Button(Const('Технічна перерва'), id='break')), state=CheckList2.cl2),
        Window(
            Const("Закриття зміни, Хештег 2.0"),
            Group(
                Column(multiselect(csv_to_list_of_tuple_text("close_check_list_2_0.csv"))),
                Button(Const('Технічна перерва'), id='break')), state=CheckList2.ccl2)
    )

    dialog3 = Dialog(
        Window(
            Const("Літній майданчик 1.0"),
            Group(
                Column(multiselect(csv_to_list_of_tuple_text("litniy_maydanchik_1_0.csv"))),
                Button(Const('Закриття зміни'), id='close', on_click=close_shift),
                Button(Const('Технічна перерва'), id='break')), state=LitniyMaydanchik1.lm1),
        Window(
            Const("Закриття зміни, Літній майданчик 1.0"),
            Group(
                Column(multiselect(csv_to_list_of_tuple_text("close_litniy_maydanchik_1_0.csv"))),
                Button(Const('Технічна перерва'), id='break')), state=LitniyMaydanchik1.clm1)
    )

    dialog4 = Dialog(
        Window(
            Const("Літній майданчик 2.0"),
            Group(
                Column(multiselect(csv_to_list_of_tuple_text("litniy_maydanchik_2_0.csv"))),
                Button(Const('Закриття зміни'), id='close', on_click=close_shift),
                Button(Const('Технічна перерва'), id='break')), state=LitniyMaydanchik2.lm2),
        Window(
            Const("Закриття зміни, Літній майданчик 2.0"),
            Group(
                Column(multiselect(csv_to_list_of_tuple_text("close_litniy_maydanchik_2_0.csv"))),
                Button(Const('Технічна перерва'), id='break')), state=LitniyMaydanchik2.clm2)
    )

    dialogs = {'hashtag_1_0': dialog1,
               'hashtag_2_0': dialog2,
               'litniy_maydanchik_1_0': dialog3,
               'litniy_maydanchik_2_0': dialog4
               }
    try:
        registry.register(dialog=dialogs[key])
    except ValueError:
        pass
    finally:
        return dialogs[key]


async def close_shift(c: types.CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.dialog().next()

