import os
from aiogram.utils import executor
import config
from create_bot import dp
from data_base import sqlite_db
from create_bot import bot
async def on_startup(dp):
    print('Бот вышел в онлайн')
    await bot.set_webhook(config.URL_APP)

async def on_shutdown(dp):
    await bot.delete_webhook()

from handlers import client, admin, other

client.register_handlers_clients(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

executor.start_webhook(
    dispatcher=dp,
    webhook_path="",
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=True,
    host="0.0.0.0",
    port=int(os.environ.get('PORT', 5000)))