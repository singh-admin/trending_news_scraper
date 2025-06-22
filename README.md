# trending_news_scraper
🔍 A FastAPI-based backend that scrapes trending news from NDTV, Times of India etc. and stores it in MongoDB for real-time access via API.

# 📰 Trending News Scraper API

A FastAPI-powered backend that scrapes the latest trending news from trusted Indian news sources like **NDTV**, **Times of India** etc, and stores them in **MongoDB** for easy access and API retrieval.

---

## 🚀 Features

- 🔍 Scrapes latest news from:
  - [NDTV](https://www.ndtv.com/latest)
  - [Times of India (TOI)](https://timesofindia.indiatimes.com/rssfeedstopstories.cms)
  - ETC
- ⚡ Fast and asynchronous API built with **FastAPI**
- 🧠 Clean architecture: scraping, database, and API logic are modular
- 🛢️ Stores scraped data in **MongoDB**
- 🔁 Supports periodic news updates
- 📦 Easily deployable with `Docker` or any cloud platform

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI**
- **BeautifulSoup4 + Requests**
- **MongoDB** (via `pymongo`)
- **Uvicorn** (for running FastAPI)

---
### ⏳ Scheduler Info

A background scheduler runs automatically every 15 minutes to:
- Scrape the latest articles from NDTV, TOI etc.
- Deduplicate and store only fresh news in MongoDB

You don’t need to manually call the `/scrape` endpoint unless you want to force an update.


## 📦 Installation

### 🔧 Prerequisites

- Python 3.10+
- MongoDB running locally or on a cloud URI

### 📥 Clone the Repository

```bash
git clone https://github.com/singh-admin/trending-news-scraper.git
cd trending-news-scraper


## 📽️ Demo

Here’s a quick demo of the trending news scraper fetching and storing data in MongoDB:

![News Scraper Demo](news_scrapper.gif)



