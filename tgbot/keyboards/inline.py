from aiogram import types

buttons = [
            types.InlineKeyboardButton(text="Купить", url="tg://resolve?domain=foxik93")
        ]
keyboard = types.InlineKeyboardMarkup()
keyboard.add(*buttons)


taxi = [
            types.InlineKeyboardButton(text="Расчитать доставку", url="https://taxi.yandex.ru/")
        ]
taxi_kb = types.InlineKeyboardMarkup()
taxi_kb.add(*taxi)