from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

start_buttons = ['🗂Меню']
keyboard = ReplyKeyboardMarkup(resize_keyboard=True,)
b1 = KeyboardButton("🛒Оформить заказ", resize_keyboard=True)
b2 = KeyboardButton('📅Режим работы',resize_keyboard=True)
b3 = KeyboardButton('🚕Доставка',resize_keyboard=True)
keyboard.add(*start_buttons).row(b1,b2,b3)


menu_buttons = ['🧁Капкейки','🎂Тортики','🍬Конфеты']
menu1 = ReplyKeyboardMarkup(resize_keyboard=True)
m1 = KeyboardButton('Вернуться',resize_keyboard=True)
menu1.add(*menu_buttons).row(m1)


adm_buttons = ['Добавить товар','Меню пользователя','Удалить']
adm = ReplyKeyboardMarkup(resize_keyboard=True)
adm.add(*adm_buttons)

del_buttons = ['Удалить Капкейки❌','Удалить Тортики❌','Удалить Конфеты❌']
del_menu = ReplyKeyboardMarkup(resize_keyboard=True)
m1 = KeyboardButton('Вернуться в админ меню',resize_keyboard=True)
del_menu.add(*del_buttons).row(m1)

menu_download = ['Добавить капкейки','Добавить тортики','Добавить конфеты']
download_m = ReplyKeyboardMarkup(resize_keyboard=True)
m1 = KeyboardButton('Вернуться в админ меню',resize_keyboard=True)
m2 = KeyboardButton('Отменить добавление',resize_keyboard=True)
download_m.add(*menu_download).row(m1,m2)