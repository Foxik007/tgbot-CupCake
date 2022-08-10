from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from data_base import sqllite_db
from tgbot.handlers.FSM.cupcake import bot1
from tgbot.keyboards.reply import adm, del_menu, download_m


async def adm_kb(message: Message):
    await message.answer('Вы вошли как администратор,что бы хотелось сделать?', reply_markup=adm)


async def del_callback_run(callback_query: types.CallbackQuery):
    await sqllite_db.sql_delete_command(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена', show_alert=True)


async def delete_item(message: types.Message):
    read = await sqllite_db.sql_read2_cupcake()
    for ret in read:
        await bot1.send_photo(message.from_user.id, ret[0],
                              f'{ret[1]}\nОписание: {ret[2]}\n<b>Цена:</b> {ret[-1]}')
        await bot1.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))

async def delete_item_cake(message: types.Message):
    read = await sqllite_db.sql_read2_cake()
    for ret in read:
        await bot1.send_photo(message.from_user.id, ret[0],
                              f'{ret[1]}\nОписание: {ret[2]}\n<b>Цена:</b> {ret[-1]}')
        await bot1.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))

async def delete_item_biscuit(message: types.Message):
    read = await sqllite_db.sql_read2_biscuit()
    for ret in read:
        await bot1.send_photo(message.from_user.id, ret[0],
                              f'{ret[1]}\nОписание: {ret[2]}\n<b>Цена:</b> {ret[-1]}')
        await bot1.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))


async def delete_menu(message: types.Message):
    await message.answer('Выберите категорию в которой хотите удалить товар:', reply_markup=del_menu)


async def return_adm_menu(message: types.Message):
    await message.answer('Выберите категорию в которой хотите удалить товар:', reply_markup=adm)

async def add_menu(message: types.Message):
    await message.answer('Выберите категорию в которой хотите удалить товар:', reply_markup=download_m)



def register_admin(dp: Dispatcher):
    dp.register_message_handler(adm_kb, commands=["admin"], is_admin=True)
    dp.register_message_handler(delete_item, Text(equals='Удалить Капкейки❌'), is_admin=True)
    dp.register_message_handler(delete_item_cake, Text(equals='Удалить Тортики❌'), is_admin=True)
    dp.register_message_handler(delete_item_biscuit, Text(equals='Удалить Конфеты❌'), is_admin=True)
    dp.register_message_handler(delete_menu, Text(equals='Удалить'), is_admin=True)
    dp.register_message_handler(add_menu, Text(equals='Добавить товар'), is_admin=True)
    dp.register_message_handler(return_adm_menu, Text(equals='Вернуться в админ меню'), is_admin=True)
    dp.register_callback_query_handler(del_callback_run, lambda x: x.data and x.data.startswith('del '))
