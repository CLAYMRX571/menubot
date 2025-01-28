from aiogram import Bot, Dispatcher
from asyncio import run
from aiogram.types import BotCommand
from aiogram.filters import Command
import func

dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(chat_id=7192104018, text="Bot ishga tushirildi! ✅")

async def shutdown_answer(bot: Bot):
    await bot.send_message(chat_id=7192104018, text="Bot ishdan to'xtadi! ❌")

async def start():
    dp.startup.register(startup_answer)
    dp.message.register(func.start_answer, Command("start"))
    dp.message.register(func.help_answer, Command("help"))
    dp.message.register(func.get_user_info)
    dp.shutdown.register(shutdown_answer)
    bot = Bot("7920759596:AAGNAmgDFeaY6eQyCWZNMz0M29Dqtf25-ik")
    await bot.set_my_commands([
        BotCommand(command="/start", description="Bot ishga tushirish"),
        BotCommand(command="/help", description="Yordam!")
    ])
    await dp.start_polling(bot, polling_timeout=1)

run(start())