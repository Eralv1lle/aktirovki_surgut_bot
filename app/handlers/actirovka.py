from aiogram import Router, F
from aiogram.filters import Command, or_f
from aiogram.types import Message

from app.services import get_actirovka_info
from app.utils import is_actirovka


actirovka_router = Router()

@actirovka_router.message(Command("актировка", "actirovka"))
async def actirovka_command(message: Message):
    await message.answer(await get_actirovka_info(), disable_web_page_preview=True, parse_mode="HTML")