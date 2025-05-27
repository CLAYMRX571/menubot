from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

async def start_command_answer(message: Message, bot: Bot):
    await message.answer("Assalomu alaykum, botdan foydalanishni bilmasangiz /help buyrug'ini yuboring")

async def help_command_answer(message: Message, bot: Bot):
    matn = """Botdan foydalanish:
    /new - Yangi ariza yuborish
    /stop - Arizani bekor qilish
    """
    await message.answer(matn)

async def new_command_answer(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Menga ism-familiyangizni yuboring.")
    await state.set_state(states.newAriza.name)

async def stop_command_answer(message: Message, bot: Bot, state: FSMContext):
    this_state = await state.get_state()
    if this_state == "None": await message.answer("Bekor qilish uchun sizda ariza mavjud emas!")
    else:
        await message.answer("Ariza bekor qilindi!")
        await state.clear()

async def newAriza_name_answer(message: Message, bot: Bot, state: FSMContext):
    if len(message.text.split()) == 2:
        if not ("0" in message.text or
            "1" in message.text or
            "2" in message.text or
            "3" in message.text or
            "4" in message.text or
            "5" in message.text or
            "6" in message.text or
            "7" in message.text or
            "8" in message.text or
            "9" in message.text):
            await state.update_data(name=message.text)
            await message.answer("Ism-familiya qabul qilindi:\n\n{message.text}")
            await message.answer("Menga yoshingizni yuboring.")
            await state.set_state(states.newAriza.age)
        else: await message.answer("Ism-familiyada raqam qatnashishi mumkin emas!")
    else: await message.asnwer("Manga faqat ism-familiyangizni yuboring")

async def newAriza_age_answer(message: Message, bot: Bot, state: FSMContext):
    if message.text.isdigit():
        if int(message.text) < 150 and int(message.text) > 0:
            await state.update_data(age=message.text)
            await message.answer(f"Yoshingiz qabul qilindi.\n\n{message.text}")
            await state.set_state(states.newAriza.phone)
        elif int(message.text) < 150: await message.answer("Man 150 yoshdan oshgan odam ariza berganiga ishonmayman.")
        else: await_message.answer("Man 0 yoshdan kichik yoshli odam ariza berganiga ishonmayman.")
    else: await message.answer("Manga yoshingizni raqamlarda kiriting.")


