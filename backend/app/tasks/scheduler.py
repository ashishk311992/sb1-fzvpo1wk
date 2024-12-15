from apscheduler.schedulers.background import BackgroundScheduler
from app.utils.email import send_expiry_notification

def init_scheduler():
    scheduler = BackgroundScheduler()
    
    # Schedule document expiry check daily at 9 AM
    scheduler.add_job(
        send_expiry_notification,
        'cron',
        hour=9,
        minute=0
    )
    
    scheduler.start()