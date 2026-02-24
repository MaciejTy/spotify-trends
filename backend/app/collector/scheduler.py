from apscheduler.schedulers.background import BackgroundScheduler

from app.collector.tasks import collect_data

import threading

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(collect_data, 'cron', hour=3, minute = 0)
    scheduler.start()

def run_initial_collect():
    thread = threading.Thread(target=collect_data, daemon=True)
    thread.start()