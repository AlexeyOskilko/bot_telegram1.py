from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import os, hashlib
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle

storage=MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot,storage=storage)


answ = dict()

#Кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Наш ютуб', url = 'https://youtube.com')
urlButton2 = InlineKeyboardButton(text='ссылка в гугле', url = 'https://google.com')
x = [InlineKeyboardButton(text='ссылка в гугле', url = 'https://google.com'), InlineKeyboardButton(text='ещё ютуб', url = 'https://youtube.com'),\
     InlineKeyboardButton(text='наш дискорд', url = 'https://discord.com')]
urlkb.add(urlButton, urlButton2).row(*x).insert(InlineKeyboardButton(text='наш сайт',url = 'https://yandex.ru'))

@dp.message_handler(commands='ссылки')
async def url_command(message : types.Message):
    await message.answer('Ссылочки', reply_markup=urlkb)

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_1' ),\
                                             InlineKeyboardButton(text='Dislike', callback_data='like_-1' ))
@dp.message_handler(commands='test')
async def test_commands(message : types.Message):
    await message.answer("За новую пиццу", reply_markup = inkb)

@dp.callback_query_handler(Text(startswith='like_')) #handler сработает и на лайк и на дислайк(одинаковые callback_data) и запустит кнопку
async def www_call(callback : types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)

@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    text = query.query or 'echo'
    link = 'https://ru.wikipedia.org/wiki/'+text
    result_id: str = hashlib.md5(text.encode()).hexdigest()

    articles = [types.InlineQueryResultArticle(
        id = result_id,
        title = 'Статья Wikipedia:',
        url=link,
        input_message_content=types.InputTextMessageContent(
            message_text=link))]

    await query.answer(articles, cache_time=1, is_personal=True)





