from aiogram import Dispatcher, types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from data_base import sqllite_db
from tgbot.config import load_config
from tgbot.misc.states import Cake

config = load_config(".env")
bot1 = Bot(token=config.tg_bot.token, parse_mode='HTML')


async def start_add(message: types.Message):
    await Cake.photo.set()
    await message.answer('Загрузите фото торта:')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await Cake.next()
    await message.answer('Введите название:')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await Cake.next()
    await message.answer('Введите описание:')


async def load_desc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['desc'] = message.text
    await Cake.next()
    await message.answer('Введите вкус:')

async def load_taste(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['taste'] = message.text
    await Cake.next()
    await message.answer('Введите цену:')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = int(message.text)
    await sqllite_db.sql_add_command2(state)
    await state.finish()
    await message.answer('Товар успешно добавлен❗')

async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Добавление отменено')


def register_cake(dp: Dispatcher):
    dp.register_message_handler(start_add, Text(equals='Добавить тортики'), is_admin=True)
    dp.register_message_handler(cancel, Text(equals='Отменить добавление'), state="*", is_admin=True)
    dp.register_message_handler(load_photo, content_types=['photo'], state=Cake.photo)
    dp.register_message_handler(load_name, state=Cake.name)
    dp.register_message_handler(load_desc, state=Cake.description)
    dp.register_message_handler(load_taste, state=Cake.taste)
    dp.register_message_handler(load_price, state=Cake.price)
