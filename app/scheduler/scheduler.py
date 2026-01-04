from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from pytz import timezone

from config import config
from app.scheduler.tasks import send_actirovka


scheduler = AsyncIOScheduler(timezone=timezone(config.TIMEZONE))

def setup_scheduler(bot: Bot):
    scheduler.add_job(
        send_actirovka,
        CronTrigger(
            day_of_week="mon-sat",
            hour=6,
            minute=30
        ),
        kwargs={"shift": 1, "bot": bot},
        id="morning_actirovka_message",
        replace_existing=True,
        misfire_grace_time=300,
        coalesce=True,
        max_instances=1
    )
    scheduler.add_job(
        send_actirovka,
        CronTrigger(
            day_of_week="mon-sat",
            hour=12,
            minute=0
        ),
        kwargs={"shift": 2, "bot": bot},
        id="day_actirovka_message",
        replace_existing=True,
        misfire_grace_time=300,
        coalesce=True,
        max_instances=1
    )

    if not scheduler.running:
        scheduler.start()