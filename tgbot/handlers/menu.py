from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data_base import sqllite_db
from tgbot.handlers.FSM.biscuit import bot1
from tgbot.keyboards.reply import menu1


async def menu(message: types.Message):
    await message.answer('Чего бы вам хотелось заказать?',reply_markup=menu1)

async def submenu_cupcake(message: types.Message):
    await sqllite_db.sql_read_cupcake(message)

async def submenu_cake(message: types.Message):
    await sqllite_db.sql_read_cake(message)

async def submenu_biscuit(message: types.Message):
    await sqllite_db.sql_read_biscuit(message)

def register_menu(dp:Dispatcher):
    dp.register_message_handler(menu,Text(equals='🗂Меню'))
    dp.register_message_handler(submenu_cupcake,Text(equals='🧁Капкейки'))
    dp.register_message_handler(submenu_cake, Text(equals='🎂Тортики'))
    dp.register_message_handler(submenu_biscuit, Text(equals='🍬Конфеты'))
