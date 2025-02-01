from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import  asyncio



api = ''
bot = Bot(token=api)
dp = Dispatcher(bot,storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
kb.add(button_1)
kb.add(button_2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weigth = State()

# kb = ReplyKeyboardMarkup(resize_keyboard=True)
# button_1 = KeyboardButton(text='Рассчитать')
# button_2 = KeyboardButton(text='Информация')
# kb.add(button_1)
# kb.add(button_2)

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = kb)

@dp.message_handler(text=['Рассчитать'])
async def start(message):

    await message.answer('Введите свой возраст: ')
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


if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)