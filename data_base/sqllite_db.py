import sqlite3 as sq

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot_start import bot
from tgbot.handlers.FSM.biscuit import bot1
from tgbot.keyboards.inline import keyboard


def sql_start():
    global cur, base
    base = sq.connect('cupcake.db')
    cur = base.cursor()
    if base:
        print('Database connected is ok')
    base.execute('CREATE TABLE IF NOT EXISTS cupcake(img TEXT,name TEXT PRIMARY KEY,description TEXT,taste TEXT,quantity INT,price INT)')
    base.execute(
        'CREATE TABLE IF NOT EXISTS cake(img TEXT,name TEXT PRIMARY KEY,description TEXT,taste TEXT,price INT)')
    base.execute(
        'CREATE TABLE IF NOT EXISTS biscuit(img TEXT,name TEXT PRIMARY KEY,description TEXT,taste TEXT,quantity INT,price INT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO cupcake VALUES (?,?,?,?,?,?)', tuple(data.values()))
        base.commit()

async def sql_add_command2(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO cake VALUES (?,?,?,?,?)', tuple(data.values()))
        base.commit()

async def sql_add_command3(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO biscuit VALUES (?,?,?,?,?,?)', tuple(data.values()))
        base.commit()

async def sql_read_cupcake(message):
    for ret in cur.execute('SELECT * FROM cupcake').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],f'<b>Название:</b> {ret[1]}\n<b>Описание:</b> {ret[2]}\n'
                                                          f'<b>Вкус:</b> {ret[3]}\n<b>Количество:</b> {ret[4]}\n<b>Цена:</b> {ret[-1]}',parse_mode='HTML',reply_markup=keyboard)

async def sql_read_cake(message):
    for ret in cur.execute('SELECT * FROM cake').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],f'<b>Название:</b> {ret[1]}\n<b>Описание:</b> {ret[2]}\n'
                                                          f'<b>Вкус:</b> {ret[3]}\n<b>Цена:</b> {ret[-1]}',parse_mode='HTML',reply_markup=keyboard)
async def sql_read_biscuit(message):
    for ret in cur.execute('SELECT * FROM biscuit').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],f'<b>Название:</b> {ret[1]}\n<b>Описание:</b> {ret[2]}\n'
                                                          f'<b>Вкус:</b> {ret[3]}\n<b>Количество:</b> {ret[4]}\n<b>Цена:</b> {ret[-1]}',parse_mode='HTML',reply_markup=keyboard)

async def sql_read2_cupcake():
    return cur.execute('SELECT * FROM cupcake').fetchall()

async def sql_read2_cake():
    return cur.execute('SELECT * FROM cake').fetchall()

async def sql_read2_biscuit():
    return cur.execute('SELECT * FROM biscuit').fetchall()


async def sql_delete_command(data):
    cur.execute('DELETE FROM cupcake WHERE name == ?',(data,))
    base.commit()