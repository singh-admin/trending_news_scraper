from fastapi import FastAPI
from .db import get_latest_news
from .scheduler import start_scheduler

app = FastAPI()

@app.on_event("startup")
def startup_event():
    # print("App is starting...")
    start_scheduler()  # This triggers the scraping job automatically

@app.get("/news")
def read_news(limit: int = 10):
    return get_latest_news(limit)


@app.get("/test-scrape")
def test_scrape():
    from .scraper import scrape_news
    from .db import save_news
    news = scrape_news()
    save_news(news)
    return {"inserted": len(news)}
