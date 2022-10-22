from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, "Приятного аппетита!",reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\n https://t.me/PizzaKroogster_bot')


# @dp.message_handler(commands=["Режим_Работы"])
async def pizza_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Режим работы: Понедельник - Пятница с 9 до 23, Суббота-Воскресенье с 10 до 23 часов')


# @dp.message_handler(commands=["Адрес"])
async def pizza_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, "Мы находимся по адресу: Сусанина 59")

@dp.message_handler(commands=["Меню"])
async def pizza_menu_command(message : types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_clients ( dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=["Расположение"])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])

