from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
from bot_token import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_inf = KeyboardButton(text="Информация")
button_res = KeyboardButton(text="Рассчитать")
kb.row(button_res,button_inf)


def activity(number):
    if number == 1:
        coefficient = 1.2
    elif number == 2:
        coefficient = 1.375
    elif number == 3:
        coefficient = 1.55
    elif number == 4:
        coefficient = 1.725
    else:
        coefficient = 1.9
    return coefficient
        

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()
    active = State()


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer("Привет! Я бот, помогающий следить за вашим здоровьем.\n "
                         "Введите команду *Calories*, чтобы рассчитать норму калорий.",
                         reply_markup=kb)


@dp.message_handler(text="Рассчитать")
async def set_sex(message):
    await message.answer('Введите ваш пол(Мужской\Женский):')
    await UserState.sex.set()

@dp.message_handler(state=UserState.sex)
async def set_age(message, state):
    await state.update_data(sex=message.text)
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_active(message, state):
    await state.update_data(weight=int(message.text))
    await message.answer('Выберите вашу активность(цифру):\n'
                         '1.Минимальная активность\n'
                         '2.Слабая активность\n'
                         '3.Средняя активность\n'
                         '4.Высокая активность\n'
                         '5.Экстра-активность(под эту категорию обычно подпадают люди,'
                         'занимающиеся, например, тяжелой атлетикой, или другими силовыми видами спорта с ежедневными тренировками, '
                         'а также те, кто выполняет тяжелую физическую работу).')
    await UserState.active.set()


@dp.message_handler(state=UserState.active)
async def send_calories(message, state):
    await state.update_data(active=int(message.text))
    date = await state.get_data()
    if date['sex'] == 'Мужской':
        await message.answer(
            f"Ваша норма калорий: {(10 * date['weight'] + 6.25 * date['growth'] + 5 * date['age'] + 5) * activity(date['active'])}")
    else:
        await message.answer(
            f"Ваша норма калорий: {(10 * date['weight'] + 6.25 * date['growth'] + 5 * date['age'] - 161) * activity(date['active'])}")
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)