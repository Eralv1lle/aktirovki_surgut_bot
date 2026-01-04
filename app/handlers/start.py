from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.messages import START_TEXT
from db import Chat

start_router = Router()

@start_router.message(CommandStart())
async def start(message: Message):
    Chat.get_or_create(
        chat_id=message.chat.id,
        defaults={
            "type": message.chat.type,
            "username": message.chat.username,
            "title": message.chat.title
        }
    )
    
    await message.answer(START_TEXT)