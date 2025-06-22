from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)

db = client["news_db"]
collection = db["trending_news"]

# Ensure index on "url" (runs once, silently skips if already exists)
collection.create_index("url", unique=True)


def save_news(news_list):
    # for news in news_list:
    #     if not collection.find_one({"title": news["title"]}):
    #         collection.insert_one(news)
    inserted_count = 0
    for news in news_list:
        existing = collection.find_one({"url": news["url"]})
        if not existing:
            collection.insert_one(news)
            inserted_count += 1
    print(f"Saved {inserted_count} new articles (ignored duplicates)")

def get_latest_news(limit=10):
    return list(collection.find().sort("fetched_at", -1).limit(limit))

