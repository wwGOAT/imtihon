from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from keyboards.default.user import user_main_menu, phone_number_share, location_share
from loader import dp, db
from aiogram import types
from utils.database import Database

from states.user import RegisterState


@dp.message_handler(commands=['start'])
async def user_start(message: types.Message):
    if db.get_user_by_chat_id(chat_id=message.chat.id):
        text = "Assalomu alaykum, xush kelibsiz"
        await message.answer(text=text, reply_markup=user_main_menu)
    else:
        text = "Assalomu alaykum, ismingizni kiriting"
        await message.answer(text=text)
        await RegisterState.full_name.set()


@dp.message_handler(state=RegisterState.full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text, chat_id=message.chat.id)

    text = "Telefon raqam"
    await message.answer(text=text, reply_markup=phone_number_share)
    await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.phone_number, content_types=types.ContentTypes.CONTACT)
async def get_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)

    text = "Manzil"
    await message.answer(text=text, reply_markup=location_share)
    await RegisterState.location.set()


@dp.message_handler(state=RegisterState.location, content_types=types.ContentTypes.LOCATION)
async def get_location(message: types.Message, state: FSMContext):
    location = f"{message.location.longitude}${message.location.latitude}"
    await state.update_data(location=location)

    data = await state.get_data()
    if db.add_user(data):
        text = "Successfully registered ✅"
    else:
        text = "Bot has some problems"
    await message.answer(text=text, reply_markup=user_main_menu)
    await state.finish()


@dp.message_handler(commands=['image'])
async def image_handler(message: types.Message):
    await message.answer_photo(photo=link, caption=text)


async def show_profile(message: types.Message):
    user_info = f"Foydalanuvchi ID: {message.from_user.id}\nIsm: {message.from_user.first_name}\nFamiliya: {message.from_user.last_name}\nUsername: @{message.from_user.username}"
    await message.answer(user_info)


@dp.message_handler(lambda message: message.text == 'Profile')
async def profile_command(message: types.Message):
    await show_profile(message)


@dp.message_handler(Command("start"))
async def start(message: Message):
    chat_id = message.chat.id
    user = db.get_user_by_chat_id(chat_id)
    if user:
        full_name = user[2]
        phone_number = user[3]
        location_name = user[4]
        await message.answer(f"Salom, {full_name}!\nSizning telefon raqamingiz: {phone_number}\nSizning manzilingiz: {location_name}")
    else:
        await message.answer("Assalomu alaykum! Siz hali ro'yxatdan o'tmadingiz.")


async def show_courses(message: types.Message):
    user_info = f"Hozircha bizda kurslar mavjud emas"
    await message.answer(user_info)


@dp.message_handler(lambda message: message.text == 'Courses')
async def profile_command(message: types.Message):
    await show_courses(message)


@dp.message_handler(Command("start"))
async def start(message: Message):
    courses = db.get_courses()
    if courses:
        await message.answer(f"Python"
                             f"C++")
    else:
        await message.answer("Hozircha bizda kurslar mavjud emas")