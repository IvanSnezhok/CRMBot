from aiogram import executor

from data.gsheet import update_all
from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify


async def on_startup(dispatcher):
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)
    update_all()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
