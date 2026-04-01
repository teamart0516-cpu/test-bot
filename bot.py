from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram import F
import asyncio
import logging
import sys


# Твой токен
TOKEN = "8514931533:AAHGQAxCPlovo-FySOy9F3OIjKiJS7NThRw"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    await message.answer(f"Привет! Я бот на новой версии aiogram, запущен 24/7!")

@dp.message()
async def echo_handler(message: types.Message):
    # Просто повторяем сообщение
    await message.send_copy(chat_id=message.chat.id)

async def main():
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
