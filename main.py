from aiogram import Bot, Dispatcher, types
from asyncio import run

dp = Dispatcher()

async def echo(message: types.Message, bot: Bot):
    await message.copy_to(chat_id=message.chat.id)

async def start():
    dp.message.register(echo)
    bot = Bot("7920759596:AAGNAmgDFeaY6eQyCWZNMz0M29Dqtf25-ik")
    await dp.start_polling(bot)

run(start())