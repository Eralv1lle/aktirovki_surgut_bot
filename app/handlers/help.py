from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.messages import HELP_TEXT

help_router = Router()

@help_router.message(Command("help"))
async def help(message: Message):
    await message.answer(HELP_TEXT)