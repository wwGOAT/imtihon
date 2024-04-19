from aiogram.dispatcher import FSMContext

from main.config import ADMINS
from keyboards.default.user import user_main_menu, phone_number_share, location_share
from loader import dp, db, bot
from aiogram import types

from states.user import RegisterState


@dp.message_handler(commands=['admin'])
async def contact_admin_handler(message: types.Message, state: FSMContext):
    text = "Habarni kiriting"
    await message.answer(text=text)
    await state.set_state('contact-admin')


@dp.message_handler(state="contact-admin")
async def contact_admin_handler(message: types.Message, state: FSMContext):
    user = db.get_user_by_chat_id(chat_id=message.chat.id)
    text = f"""
{user[1]}
{user[2]}

{message.text}
"""
    await bot.send_message(chat_id=ADMINS, text=text)
    text = "Habar adminga yuborildi"
    await message.answer(text=text)
    await state.finish()


@dp.callback_query_handler()
async def admin_reply_handler(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await state.update_data(send_chat_id=callback_data['chat_id'])
    text = "Javobingizni kiring"
    await call.message.answer(text=text)
    await state.set_state('admin-reply')


@dp.message_handler(state="admin-reply")
async def admin_reply_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    send_chat_id = data['send_chat_id']
    await bot.send_message(chat_id=send_chat_id, text=message.text)
    text = "Habar yuborildi"
    await message.answer(text=text)
    await state.finish()
