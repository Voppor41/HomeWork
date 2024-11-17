from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
from bot_token import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()
    active = State()


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer("Привет! Я бот, помогающий следить за вашим здоровьем.\n "
                        "Введите команду *Calories*, чтобы рассчитать норму калорий.")


@dp.message_handler(text="Calories")
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
        if date['active'] == 1:
            await message.answer(
                f"Ваша норма калорий: {(10 * date['weight'] + 6.25 * date['growth'] + 5 * date['age'] + 5)* 1.2}")
        elif date['active'] == 2:
            await message.answer(
                f"Ваша норма калорий: {(10 * date['weight'] + 6.25 * date['growth'] + 5 * date['age'] + 5) * 1.375}")
        elif date['active'] == 3:
            await message.answer(
                f"Ваша норма калорий: {(10 * date['weight'] + 6.25 * date['growth'] + 5 * date['age'] + 5) * 1.55}")
        elif date['active'] == 4:
            await message.answer(
                f"Ваша норма калорий: {(10 * date['weight'] + 6.25 * date['growth'] + 5 * date['age'] + 5) * 1.725}")
        else:
            await message.answer(
                f"Ваша норма калорий: {(10 * date['weight'] + 6.25 * date['growth'] + 5 * date['age'] + 5) * 1.9}")
    else:
        if date['active'] == 1:
            await message.answer(
                f"Ваша норма калорий: {(10 * date['weight'] + 6.25 * date['growth'] + 5 * date['age'] - 161) * 1.2}")
        elif date['active'] == 2:
            await message.answer(
                f"Ваша норма калорий: {(10 * date['weight'] + 6.25 * date['growth'] + 5 * date['age'] - 161) * 1.375}")
        elif date['active'] == 3:
            await message.answer(
                f"Ваша норма калорий: {(10 * date['weight'] + 6.25 * date['growth'] + 5 * date['age'] - 161) * 1.55}")
        elif date['active'] == 4:
            await message.answer(
                f"Ваша норма калорий: {(10 * date['weight'] + 6.25 * date['growth'] + 5 * date['age'] - 161) * 1.725}")
        else:
            await message.answer(
                f"Ваша норма калорий: {(10 * date['weight'] + 6.25 * date['growth'] + 5 * date['age'] - 161) * 1.9}")
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
