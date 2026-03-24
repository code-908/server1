import asyncio
from os import name
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import os
from dotenv import load_dotenv
load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()
dp.message(CommandStart())
async def start(message:Message):
    await message.answer('Hello')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())