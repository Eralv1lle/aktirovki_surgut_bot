from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode

from app.services import get_actirovka_info
from config import config


async def send_actirovka(bot: Bot):
    text = await get_actirovka_info()

    for chat_id in config.CHAT_IDS:
        try:
            await bot.send_message(chat_id, text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
        except Exception:
            pass
