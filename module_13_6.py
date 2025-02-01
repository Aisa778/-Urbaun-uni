from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import  asyncio



api = ''
bot = Bot(token=api)
dp = Dispatcher(bot,storage=MemoryStorage())

kb_1 = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
kb_1.add(button_1)
kb_1.add(button_2)

kb_2 = InlineKeyboardMarkup()
button_1 = InlineKeyboardButton(text='Рассчитать формулу калорий', callback_data='calories')
button_2 = InlineKeyboardButton(text='Формулы рассчета', callback_data='formulas')
kb_2.add(button_1)
kb_2.add(button_2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weigth = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = kb_1)

@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст: ')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message,state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост в см')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес в кг')
    await UserState.weigth.set()


@dp.message_handler(state=UserState.weigth)
async def send_message(message,state):
    calorie = 0.01
    await state.update_data(weigth=message.text)
    data= await state.get_data()
    calorie=10*int(data['weigth'])+6.25*int(data['growth'])-5*int(data['age'])
    await message.answer(f'Ваша норма калорий составляет {calorie}')
    await state.finish()

@dp.message_handler(text='Информация')
async def info_message(message):
    await message.answer('Этот Бот для рассчета нормы калорий у женщин')


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию',reply_markup = kb_2)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.')
    await call.answer()




if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)