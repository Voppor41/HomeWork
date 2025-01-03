from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from token import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


#@dp.message_handler(text = ['Uraban', 'ff'])
#async def urban_message(message):
#    print("Urban message")

@dp.message_handler(commands=['start'])
async def start_message(message):
    print("Start message")
    print("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler()
async def all_message(message):
    print("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
