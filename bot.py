import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import ChatJoinRequest


RAW_TOKENS = os.getenv("TOKEN", "")  #ТОКЕНЫ
TOKENS = [t.strip() for t in RAW_TOKENS.split(",") if t.strip()]

async def start_single_bot(token):
    """Функция запуска одного конкретного бота"""
    bot = Bot(token=token)
    dp = Dispatcher()


    @dp.chat_join_request()
    async def approve_request(chat_join: types.ChatJoinRequest):
        try:
            await chat_join.approve()
            logging.info(f"Бот {token[:10]}... одобрил заявку юзера {chat_join.from_user.id}")
        except Exception as e:
            logging.error(f"Ошибка в боте {token[:10]}: {e}")

    try:
        logging.info(f"Запуск бота: {token[:10]}...")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

async def main():

    logging.basicConfig(level=logging.INFO)
    
    if not TOKENS:
        print("ОШИБКА: Список токенов пуст! Добавь их в Environment Variables через запятую.")
        return


    tasks = [start_single_bot(token) for token in TOKENS]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Все боты остановлены.")
