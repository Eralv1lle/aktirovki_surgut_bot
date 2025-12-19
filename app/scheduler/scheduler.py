from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import timezone

from config import config
from app.scheduler.tasks import send_actirovka


scheduler = AsyncIOScheduler(timezone=config.TIMEZONE)

def setup_scheduler(bot: Bot):
    scheduler.add_job(
        send_actirovka,
        CronTrigger(
            day_of_week="mon-sat",
            hour=20,
            minute=44
        ),
        kwargs={"bot": bot},
        id="daily_actirovka_message",
        replace_existing=True
    )
    scheduler.start()