from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode

from app.services import get_actirovka_info, get_chats_for_shift


async def send_actirovka(shift: int, bot: Bot):
    text = await get_actirovka_info()
    chats = get_chats_for_shift(shift)

    for chat in chats:
        try:
            await bot.send_message(chat.chat_id, text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
        except Exception:
            pass
