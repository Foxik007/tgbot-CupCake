from aiogram.dispatcher.filters.state import State, StatesGroup


class Cupcake(StatesGroup):
    photo = State()
    name = State()
    description = State()
    taste = State()
    quantity = State()
    price = State()

class Cake(StatesGroup):
    photo = State()
    name = State()
    description = State()
    taste = State()
    price = State()

class Biscuit(StatesGroup):
    photo = State()
    name = State()
    description = State()
    taste = State()
    quantity = State()
    price = State()