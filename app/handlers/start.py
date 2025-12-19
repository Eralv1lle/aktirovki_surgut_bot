from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.messages import START_TEXT

start_router = Router()

@start_router.message(CommandStart())
async def start(message: Message):
    await message.answer(START_TEXT)