from aiogram import Router
from aiogram.types import Message

from app.services import get_actirovka_info
from app.utils import is_actirovka


fallback_router = Router()


@fallback_router.message()
async def fallback_handler(message: Message):
    if message.chat.type != "private":
        return

    if message.text.startswith("/"):
        return

    if is_actirovka(message.text):
        await message.answer(
            await get_actirovka_info(),
            disable_web_page_preview=True,
            parse_mode="HTML"
        )
    else:
        await message.answer(
            "Я могу подсказать по актировке ❄️\n"
            "Напиши «актировка» или используй /actirovka"
        )
