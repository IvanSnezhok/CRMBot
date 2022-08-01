from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from aiogram_dialog import DialogManager, StartMode

from keyboards.default.keyboard import auth_contact, main_menu, geo_send, add_money, remove_keyboard
from keyboards.inline.keyboard import location, check_lists_read
from loader import dp, db
from states.diaolg_states import DialogStates
from utils.check_lists import dialogs_manager


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"""Привіт👋🏻 {message.from_user.full_name}!
Вітаємо тебе у боті. Тут є уся інформація, яка полегшить тобі роботу щодня🔥
Надішли свій номер телефону для того, щоб авторизуватись за допомогою кнопки знизу""",
                         reply_markup=auth_contact)
    await state.set_state('auth')


@dp.message_handler(state='auth')
async def auth_text(message: types.Message):
    await message.answer("Надішли свій номер телефону для того, щоб авторизуватись за допомогою кнопки знизу",
                         reply_markup=auth_contact)


@dp.message_handler(content_types=types.ContentTypes.CONTACT, state='auth')
async def auth_tel(message: types.Message, state: FSMContext):
    await message.answer("Вітаємо вас в боті! Тепер ви можете продовжувати роботу з ботом🤖",
                         reply_markup=main_menu)
    await state.finish()


@dp.message_handler(text="База знань")
async def base_knowledge(message: types.Message):
    await message.answer("Тут буде зберігатись різна інформація про компанію (Brand book),"
                         " телеграфи про вирішення конфліктів, інфо як навчання як продавати краще,"
                         " перезнтації різні і т.д. ",
                         reply_markup=main_menu)


@dp.message_handler(text="Чек листи")
async def check_list(message: types.Message, state: FSMContext):
    await message.answer("Виберіть потрібний чек-лист", reply_markup=check_lists_read)
    await state.set_state('check_lists_read')


@dp.message_handler(text="Мої гроші")
async def my_money(message: types.Message):
    try:
        try:
            money_result = await db.get_money(message.from_user.id)
        except Exception as e:
            print(e)
            money_result = 0
        money_text = []
        all_money = 0.0
        if money_result is not 0:
            for date, money in money_result.items():
                money_text.append(f"{date} - {money}")
                all_money += float(money)
            await message.answer("Мої гроші:\n" + "\n".join(money_text))
            await message.answer(f"Всього грошей: {all_money}", reply_markup=add_money)
        else:
            await message.answer("У системі не зареєстровані ваші гроші🤔\n"
                                 "Можете їх додати по кнопці знизу!", reply_markup=add_money)
    except Exception as e:
        print(e)
        await message.answer("Виникла помилка, спробуйте пізніше🤔", reply_markup=main_menu)


@dp.message_handler(text="Додати гроші")
async def add_my_money(message: types.Message, state: FSMContext):
    await message.answer("Введіть кількість грошей\n"
                         "Наприклад:\n"
                         "123.50 або 200", reply_markup=remove_keyboard)
    await state.set_state('add_money')


@dp.message_handler(state='add_money')
async def add_money_text(message: types.Message, state: FSMContext):
    await db.add_money(telegram_id=message.from_user.id, money=message.text, date=datetime.now())
    await message.answer("Гроші додано", reply_markup=main_menu)
    try:
        money_result = await db.get_money(message.from_user.id)
    except Exception as e:
        print(e)
        money_result = 0
    money_text = []
    all_money = 0.0
    if money_result is not 0:
        for date, money in money_result.items():
            money_text.append(f"{date} - {money}")
            all_money += float(money)
        await message.answer("Мої гроші:\n" + "\n".join(money_text))
        await message.answer(f"Всього грошей: {all_money}", reply_markup=add_money)
    await state.finish()


@dp.message_handler(text='Зміна')
async def work_time(message: types.Message):
    await message.answer('Привіт👋🏻 Поділись гео-локацією', reply_markup=geo_send)


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def work_time_place(message: types.Message):
    await message.answer('Тепер обери зал, в якому сьогодні працюєш 💪🏻', reply_markup=location)


@dp.callback_query_handler(lambda call: call.data in ['hashtag_1_0', 'hashtag_2_0',
                                                      'litniy_maydanchik_1_0', 'litniy_maydanchik_2_0'])
async def hashtag_callback(call: types.CallbackQuery, state: FSMContext, dialog_manager: DialogManager):
    await call.message.answer(f"Ви обрали локацію: {call.data}")
    await dialogs_manager(call.data)
    if call.data == 'hashtag_1_0':
        await dialog_manager.start(state=DialogStates.cl1, mode=StartMode.RESET_STACK)
    elif call.data == 'hashtag_2_0':
        await dialog_manager.start(state=DialogStates.cl2, mode=StartMode.RESET_STACK)
    elif call.data == 'litniy_maydanchik_1_0':
        await dialog_manager.start(state=DialogStates.lm1, mode=StartMode.RESET_STACK)
    elif call.data == 'litniy_maydanchik_2_0':
        await dialog_manager.start(state=DialogStates.lm2, mode=StartMode.RESET_STACK)

