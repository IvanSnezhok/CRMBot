import operator

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Multiselect, Button, Group, Column
from aiogram_dialog.widgets.text import Format, Const

from data.gsheet import update_all
from loader import db, dp, registry

from states.diaolg_states import DialogStates


def csv_to_list_of_tuple(csv):
    """
    Return item from csv with index 0 and 1
    """
    with open(csv, 'r') as f:
        return [tuple((y, x)) for x, y in enumerate(f.readlines())]


async def multiselect(items):
    buttons = Multiselect(
        checked_text=Format('✓ {item[0]}'),
        unchecked_text=Format('✖ {item[0]}'),
        id='multiselect',
        item_id_getter=operator.itemgetter(1),
        items=items,
    )
    return buttons


async def dialogs_manager(key: str):
    await update_all()
    dialog1 = Dialog(
        Window(
            Const("Ваш Чек-лист 1.0"),
            Group(
                Column(await multiselect(csv_to_list_of_tuple("check_list_1_0.csv")), ),
                Button(Const('Закриття зміни'), id='close'),
                Button(Const('Технічна перерва'), id='break')), state=DialogStates.cl1))

    dialog2 = Dialog(
        Window(
            Const("Ваш Чек-лист 2.0"),
            Group(
                Column(await multiselect(csv_to_list_of_tuple("check_list_2_0.csv")), ),
                Button(Const('Закриття зміни'), id='close'),
                Button(Const('Технічна перерва'), id='break')), state=DialogStates.cl2))

    dialog3 = Dialog(
        Window(
            Const("Літній майданчик 1.0"),
            Group(
                Column(await multiselect(csv_to_list_of_tuple("litniy_maydanchik_1_0.csv")), ),
                Button(Const('Закриття зміни'), id='close'),
                Button(Const('Технічна перерва'), id='break')), state=DialogStates.lm1))

    dialog4 = Dialog(
        Window(
            Const("Літній майданчик 2.0"),
            Group(
                Column(await multiselect(csv_to_list_of_tuple("litniy_maydanchik_2_0.csv")), ),
                Button(Const('Закриття зміни'), id='close'),
                Button(Const('Технічна перерва'), id='break')), state=DialogStates.lm2))

    dialog5 = Dialog(
        Window(
            Const("Закриття зміни, Хештег 1.0"),
            Group(
                Column(await multiselect(csv_to_list_of_tuple("close_check_list_1_0.csv")), ),
                Button(Const('Закриття зміни'), id='close'),
                Button(Const('Технічна перерва'), id='break')), state=DialogStates.ccl1))

    dialog6 = Dialog(
        Window(
            Const("Закриття зміни, Хештег 2.0"),
            Group(
                Column(await multiselect(csv_to_list_of_tuple("close_check_list_2_0.csv")), ),
                Button(Const('Закриття зміни'), id='close'),
                Button(Const('Технічна перерва'), id='break')), state=DialogStates.ccl2))

    dialog7 = Dialog(
        Window(
            Const("Закриття зміни, Літній майданчик 1.0"),
            Group(
                Column(await multiselect(csv_to_list_of_tuple("close_litniy_maydanchik_1_0.csv")), ),
                Button(Const('Закриття зміни'), id='close'),
                Button(Const('Технічна перерва'), id='break')), state=DialogStates.clm1))

    dialog8 = Dialog(
        Window(
            Const("Закриття зміни, Літній майданчик 2.0"),
            Group(
                Column(await multiselect(csv_to_list_of_tuple("close_litniy_maydanchik_2_0.csv")), ),
                Button(Const('Закриття зміни'), id='close'),
                Button(Const('Технічна перерва'), id='break')), state=DialogStates.clm2))

    dialogs = {'hashtag_1_0': dialog1,
               'hashtag_2_0': dialog2,
               'litniy_maydanchik_1_0': dialog3,
               'litniy_maydanchik_2_0': dialog4,
               'close_lists_1_0': dialog5,
               'close_lists_2_0': dialog6,
               'close_maydanchik_1_0': dialog7,
               'close_maydanchik_2_0': dialog8}
    registry.register(dialog=dialogs[key])
    return dialogs[key]
