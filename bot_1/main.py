import os
import asyncio
from loguru import logger
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")


async def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH-MM-SS} | {level} | {message}",
               rotation="3 days",
               backtrace=True,
               diagnose=True)

    bot = Bot(TOKEN)
    logger.info("Бот создан!")
    dp = Dispatcher()
    logger.info("Диспетчер создан!")

    @dp.message(Command("start"))
    async def send_welcome(message: types.Message):
        await message.answer("Привет, я МоНсТеР ПуТхОн и я эхо-бот!")
        await message.answer("Мои команды: /start и /help")
        logger.info('Бот ответил на команду /start')

    @dp.message(Command("help"))
    async def help_function(message: types.Message):
        await message.answer("Пока что я могу только отправить тебе твоё же "
                             "сообщение ведь я эхо-бот, но я стану умнее!!!")
        logger.info('Бот объяснил пользователю что может.')

    @dp.message()
    async def echo(message: types.Message):
        await message.answer(message.text)
        logger.info("Бот вернул пользователю его сообщение")

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
