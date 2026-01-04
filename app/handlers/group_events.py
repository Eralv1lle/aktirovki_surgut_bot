from aiogram import Router
from aiogram.types import Message, ChatMemberUpdated

from db import Chat

group_router = Router()


@group_router.my_chat_member()
async def bot_status(event: ChatMemberUpdated):
    chat = event.chat
    status = event.new_chat_member.status

    chat_obj, _ = Chat.get_or_create(
        chat_id=chat.id,
        defaults={
            "type": chat.type,
            "title": chat.title,
        }
    )

    if status == "administrator":
        chat_obj.is_admin = True
        chat_obj.is_active = True
        chat_obj.save()

        await event.bot.send_message(
            chat.id,
            "✅ Спасибо за права администратора! Теперь я могу рассылать актировки."
        )

    elif status in ("member", "left"):
        chat_obj.is_admin = False
        chat_obj.is_active = False
        chat_obj.save()