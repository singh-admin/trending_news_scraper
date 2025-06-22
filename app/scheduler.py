import logging
from apscheduler.schedulers.background import BackgroundScheduler
from .scraper import scrape_news
from .db import save_news

# Used looger for DEBUG
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def start_scheduler():
    logger.info("Scheduler starting...")
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, "interval", minutes=15)  # every 15 minutes
    scheduler.start()
    logger.info("Scheduler started")

def job():
    logger.info("Scraping job running...")
    news = scrape_news()
    save_news(news)
    logger.info(f"Saved {len(news)} articles")
