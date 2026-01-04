from db import Chat


def get_chats_for_shift(shift: int):
    if shift == 1:
        return Chat.select().where(
            Chat.notify_shift_1 == True,
            Chat.is_active == True
        )
    else:
        return Chat.select().where(
            Chat.notify_shift_2 == True,
            Chat.is_active == True
        )