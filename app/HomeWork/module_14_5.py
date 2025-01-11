from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from bot_token import BOT_TOKEN
from crud_functions import *

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_inf = KeyboardButton(text="Информация")
button_res = KeyboardButton(text="Рассчитать")
button_buy = KeyboardButton(text="Купить")
button_reg = KeyboardButton(text="Регистрация")
kb.row(button_res, button_inf)
kb.add(button_buy, button_reg)


ikb = InlineKeyboardMarkup(terminal_size=True)
ikb_products = InlineKeyboardMarkup(terminal_size=True)
ibutton_res = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
ibutton_for = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
ibutton_prod1 = InlineKeyboardButton(text="Протеин", callback_data="product_buying")
ibutton_prod2 = InlineKeyboardButton(text="Креатин", callback_data="product_buying")
ibutton_prod3 = InlineKeyboardButton(text="Тренболон", callback_data="product_buying")
ibutton_prod4 = InlineKeyboardButton(text="BCAA", callback_data="product_buying")
ikb.row(ibutton_res, ibutton_for)
ikb_products.row(ibutton_prod1, ibutton_prod2, ibutton_prod3, ibutton_prod4)

initiate_db()
#add_test_products()

def convertor(text):
    if ',' in text:
        return text.replace(',', '.')
    else:
        return text


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

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer("Привет! Я бот, помогающий следить за вашим здоровьем.\n "
                         "Нажмите кнопку Расчитать, чтобы рассчитать норму калорий.",
                         reply_markup=kb)

@dp.message_handler(text="Регистрация")
async def sign_up(message):
    await message.answer("Введите имя пользователя(только латинские буквы")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    username = message.text.strip()  # Убираем лишние пробелы

    if not username.isalnum():  # Проверяем, что имя содержит только буквы и цифры
        await message.answer("Имя пользователя должно содержать только латинские буквы и цифры. Попробуйте снова:")
        return

    if not is_included(username):
        await state.update_data(username=username)
        await message.answer("Введите ваш email:")
        await RegistrationState.email.set()
    else:
        await message.answer("Пользователь существует, введите другое имя.")

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    email = message.text.strip()

    if "@" not in email or "." not in email:  # Примитивная проверка email
        await message.answer("Введите корректный email:")
        return

    await state.update_data(email=email)
    await message.answer("Введите ваш возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    try:
        age = int(message.text)
        if age <= 0:
            ValueError()

    except ValueError:
        await message.answer("Введите корректный возраст")
        return

    await state.update_data(age=age)
    date = await state.get_data()
    add_users(date['username'], date['email'], date['age'])
    await state.finish()
    await message.answer("Регистрация прошла усппешно!")



@dp.message_handler(text="Информация")
async def inform_message(message):
    await message.answer("Я бот, помогающий следить за вашим здоровьем.\n"
                         "Нажмите кнопку Расчитать, чтобы рассчитать норму калорий.\n"
                         "Нажмите кнопку Купить, чтобы просмотреть доступные товары.")

@dp.message_handler(text="Купить")
async def get_buying_list(message):
    products = get_all_products()

    if not products:
        await message.answer("В данный момент все товары раскупили")
        return

    for product in products:
        title, description, price, image_url = product
        if image_url:
            await bot.send_photo(
                chat_id=message.chat.id,
                photo=image_url,
                caption=f"Название: {title}\nОписание: {description}\nЦена: {price}₽"
            )
        else:
            await message.answer(f"Название: {title}\nОписание: {description}\nЦена: {price}₽")

    await message.answer("Выберите продукт для покупки:", reply_markup=ikb_products)


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=ikb)


@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("для мужчин: (10 x вес (кг) + 6.25 x рост (см) – 5 x возраст (г) + 5) x A;\n"
                              "для женщин: (10 x вес (кг) + 6.25 x рост (см) – 5 x возраст (г) – 161) x A.\n"
                              "\nA – это уровень активности человека, его различают обычно по пяти степеням физических нагрузок в сутки:\n"
                              "\nМинимальная активность: A = 1,2.\n"
                              "Слабая активность: A = 1,375.\n"
                              "Средняя активность: A = 1,55.\n"
                              "Высокая активность: A = 1,725.\n"
                              "Экстра-активность: A = 1,9 (под эту категорию обычно подпадают люди, занимающиеся, например, тяжелой атлетикой, или другими силовыми видами спорта с ежедневными тренировками, а также те, кто выполняет тяжелую физическую работу).")


@dp.callback_query_handler(text="calories")
async def set_sex(call):
    await call.message.answer('Введите ваш пол(Мужской\Женский):')
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
    await state.update_data(weight=float(convertor(message.text)))
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
            f"Ваша норма калорий: {int((10 * date['weight'] + 6.25 * date['growth'] + 5 * date['age'] + 5) * activity(date['active']))}ккал")
    else:
        await message.answer(
            f"Ваша норма калорий: {int((10 * date['weight'] + 6.25 * date['growth'] + 5 * date['age'] - 161) * activity(date['active']))}ккал")
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)