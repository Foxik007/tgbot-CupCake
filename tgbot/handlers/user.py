
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from tgbot.keyboards.inline import taxi_kb
from tgbot.keyboards.reply import keyboard


async def start(message: Message):
    await message.answer('Выберите пункт меню:', reply_markup=keyboard)

async def back(message: Message):
    await message.answer('Главное меню',reply_markup=keyboard)

async def delivery(message: Message):
    await message.answer('Доставка осуществляется сервисом Yandex Taxi\n'
                         'С адреса г.Москва ул.Тверская д.21\n'
                         'Рассчитать сумму доставки можно по ссылке ниже',reply_markup=taxi_kb)

async def operating_mode(message: Message):
    await message.answer('Мы работаем c ежедневно с 10:00 до 22:00')

async def order(message: Message):
    await message.answer('Для согласования деталей заказа и покупки отправьте номер выбранного вами товара в личное сообщение @Foxik93')


def register_user(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(start, Text(equals='Меню пользователя'))
    dp.register_message_handler(delivery, Text(equals='🚕Доставка'))
    dp.register_message_handler(operating_mode, Text(equals='📅Режим работы'))
    dp.register_message_handler(order, Text(equals='🛒Оформить заказ'))
    dp.register_message_handler(back, Text(equals='Вернуться'))
