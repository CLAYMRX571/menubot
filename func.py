from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import states

async def start_command_answer(message: Message, bot: Bot):
    await message.answer("Assalomu alaykum, botdan foydalanishni bilmasangiz /help buyrug'ini yuboring")

async def help_command_answer(message: Message, bot: Bot):
    matn = """Botdan foydalanish:
    /new - Yangi ariza yuborish
    /stop - Arizani bekor qilish
    """
    await message.answer(matn)

async def new_command_answer(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Manga ism-familiyangizni yuboring.")
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
            await message.answer(f"Ism-familiya qabul qilindi.\n\n{message.text}")
            await message.answer("Manga yoshingizni yuboring.")
            await state.set_state(states.newAriza.age)
        else: await message.answer("Ism-familiyada raqam qatnashishi mumkin emas!")
    else: await message.answer("Manga faqat ism-familiyangizni yuboring")

async def newAriza_age_answer(message: Message, bot: Bot, state: FSMContext):
    if message.text.isdigit():
        if int(message.text) < 150 and int(message.text) > 7:
            await state.update_data(age=message.text)
            await message.answer(f"Yoshingiz qabul qilindi.\n\n{message.text}")
            await message.answer("Telefon raqamingizni kiriting.")
            await state.set_state(states.newAriza.phone)
        elif int(message.text) > 150 and int(message.text) > 7: await message.answer("Man 150 yoshdan oshgan odam ariza berganiga ishonmayman.")
        else: await message.answer("Man 7 yoshdan kichiklarni qabul qilmayman.")
    else: await message.answer("Manga yoshingizni raqamlarda kiriting.")

async def newAriza_phone_answer(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer(f"Telefon raqamingiz qabul qilindi!\n\n{message.text}")
    await message.answer("Kasbingiz nima?")
    await state.set_state(states.newAriza.job)

async def newAriza_job_answer(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(job=message.text)
    await message.answer(f"Kasbingiz qabul qilindi!\n\n{message.text}")
    await message.answer("Maqsadingiz nima?")
    await state.set_state(states.newAriza.goal)

async def newAriza_goal_answer(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(goal=message.text)
    await message.answer(f"Maqsadingiz qabul qilindi!\n\n{message.text}")
    data = await state.get_data()
    ariza = (f"Ariza beruvchi: {data.get('name')}\n"
            f"Yoshi:{data.get('age')}\n"
            f"Username: @{message.from_user.username}\n"
            f"Telefon raqami: {data.get('phone')}\n"
            f"Kasbi: {data.get('job')}\n"
            f"Maqsad: {message.text}\n")
    await message.answer(f"Arizani jo'nataymi?\n\n{ariza}\n\nHa yoki /stop deb javob bering!")
    await state.set_state(states.newAriza.verify)

async def newAriza_verify_answer(message: Message, bot: Bot, state: FSMContext):
    if message.text.lower() == "ha":
        data = await state.get_data()
        ariza = (f"Ariza beruvchi: {data.get('name')}\n"
            f"Yoshi:{data.get('age')}\n"
            f"Username: @{message.from_user.username}\n"
            f"Telefon raqami: {data.get('phone')}\n"
            f"Kasbi: {data.get('job')}\n"
            f"Maqsad: {data.get('goal')}\n")
        await bot.send_message(chat_id=7192104018, text=f"Yangi ariza:\n\n{ariza}")
        await message.answer("Arizangiz qabul qilindi!✅")
        await state.clear()
    else: await message.answer("Yo manga ha deng yoki /stop buyrug'ini yuboring!")
