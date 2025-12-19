from aiogram import Router, F
from aiogram.filters import Command, or_f
from aiogram.types import Message

from app.services import get_actirovka_info

actirovka_router = Router()

@actirovka_router.message(
    or_f(
        Command("актировка", "actirovka"),
        F.text.lower() == "актировка"
    )
)
async def start(message: Message):
    await message.answer(get_actirovka_info(), disable_web_page_preview=True, parse_mode="HTML")