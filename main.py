from aiogram import Bot, Dispatcher
from asyncio import run
from func import get_user_info

dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(chat_id=7192104018, text="Bot ishga tushirildi! ✅")

async def shutdown_answer(bot: Bot):
    await bot.send_message(chat_id=7192104018, text="Bot ishdan to'xtadi! ❌")

async def start():
    dp.startup.register(startup_answer)
    dp.message.register(get_user_info)
    dp.shutdown.register(shutdown_answer)
    bot = Bot("7920759596:AAGNAmgDFeaY6eQyCWZNMz0M29Dqtf25-ik")
    await dp.start_polling(bot, polling_timeout=1)

run(start())