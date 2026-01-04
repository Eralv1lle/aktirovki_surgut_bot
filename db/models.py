from peewee import *
from .base import db
from datetime import datetime


class BaseModel(Model):
    class Meta:
        database = db


class Chat(BaseModel):
    chat_id = BigIntegerField(unique=True)
    type = CharField()
    title = CharField(null=True)
    username = CharField(null=True)

    notify_shift_1 = BooleanField(default=True)
    notify_shift_2 = BooleanField(default=True)

    is_admin = BooleanField(default=False)
    is_active = BooleanField(default=True)

    created_at = DateTimeField(default=datetime.now)