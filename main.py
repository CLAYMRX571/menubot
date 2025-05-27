from aiogram import Bot, Dispatcher
from asyncio import run
from aiogram.types import BotCommand
from aiogram.filters import Command
import func
import states

dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(chat_id=7192104018, text="Bot ishga tushirildi! ✅")

async def shutdown_answer(bot: Bot):
    await bot.send_message(chat_id=7192104018, text="Bot ishdan to'xtadi! ❌")

async def start():
    dp.startup.register(startup_answer)
    dp.message.register(func.start_command_answer, Command("start"))
    dp.message.register(func.help_command_answer, Command("help"))
    dp.message.register(func.new_command_answer, Command("new"))
    dp.message.register(func.stop_command_answer, Command("stop"))
    dp.message.register(func.newAriza_name_answer, states.newAriza.name)
    dp.message.register(func.newAriza_age_answer, states.newAriza.age)
    dp.shutdown.register(shutdown_answer)
    bot = Bot("7920759596:AAGtqYvwsuXyHlBIqiBt41_jVNcplo4jt1c")
    await bot.set_my_commands([
        BotCommand(command="/new", description="Yangi ariza yuborish"),
        BotCommand(command="/stop", description="Arizani bekor qilish"),
        BotCommand(command="/help", description="Botdan foydalanishda yordam")
    ])

    await dp.start_polling(bot, polling_timeout=1)

run(start())