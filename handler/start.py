from aiogram.types import Message
from loader import dp
from aiogram import types

text = """
<b>Salom, {first_name}!</b>
Sizning user ID: <code>{user_id}</code>
Username: @{username}
"""

@dp.message_handler(commands=['start'])
async def start_handler(message: Message):
    first_name = message.from_user.first_name
    user_id = message.from_user.id
    username = message.from_user.username
    print(message)

    await message.answer(
        text=text.format(
            first_name=first_name,
            user_id=user_id,
            username=username
        ),
        parse_mode="HTML"
    )


