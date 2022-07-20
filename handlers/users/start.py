from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.keyboard import auth_contact, main_menu, geo_send, location
from loader import dp


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


@dp.message_handler(text='Зміна')
async def work_time(message: types.Message):
    await message.answer('Привіт👋🏻 Поділись гео-локацією', reply_markup=geo_send)


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def work_time_place(message: types.Message):
    await message.answer('Тепер обери зал, в якому сьогодні працюєш 💪🏻', reply_markup=location)


@dp.callback_query_handler(lambda call: call.data in ['hashtag_1_0', 'hashtag_2_0', 'litniy_maydanchik_1_0', 'litniy_maydanchik_2_0'])
async def hashtag_callback(call: types.CallbackQuery):
    await call.message.answer(f"Ви обрали гео-локацію: {call.data}")
    if call.data == 'hashtag_1_0':
        await call.message.edit_text(f"Чек лист 1.0", reply_markup=main_menu)
    await call.message.edit_text(f"", reply_markup=main_menu)

