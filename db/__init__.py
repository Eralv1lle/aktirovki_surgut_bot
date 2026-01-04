from .base import db
from .models import Chat


def init_db():
    db.connect(reuse_if_open=True)
    db.create_tables([Chat], safe=True)