import requests
from bs4 import BeautifulSoup
from datetime import datetime


# Scraping the BBC news
def scrape_bbc():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = []
    for item in soup.find_all("a"):
        title = item.get_text(strip=True)
        link = item.get("href")

        if not title or not link or not "/news" in link:
            continue

        if not link.startswith("http"):
            link = "https://www.bbc.com" + link

        articles.append({
            "title": title,
            "url": link,
            "source": "BBC",
            "fetched_at": datetime.utcnow()
        })

    return articles

# Scraping the NDTV news 
def scrape_ndtv():
    url = "https://www.ndtv.com/latest"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = []
    for item in soup.select("h2 a"):
        title = item.get_text(strip=True)
        link = item.get("href")

        if not title or not link:
            continue

        articles.append({
            "title": title,
            "url": link,
            "source": "NDTV",
            "fetched_at": datetime.utcnow()
        })

    return articles

# Scraping the TIMES OF INDIA news
def scrape_timesofindia():
    url = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml-xml")

    articles = []
    for item in soup.find_all("item"):  # TOI news link pattern
        title = item.title.text
        link = item.link.text

        articles.append({
            "title": title,
            "url": link,
            "source": "Times of India",
            "fetched_at": datetime.utcnow()
        })

    return articles


# Scrape from multiple sources.
def scrape_news():
    all_articles = []

    try:
        all_articles.extend(scrape_bbc())
    except Exception as e:
        print("BBC scrape failed:", e)

    try:
        all_articles.extend(scrape_ndtv())
    except Exception as e:
        print("NDTV scrape failed:", e)
        
    try:
        all_articles.extend(scrape_timesofindia())
    except Exception as e:
        print("TIMES OF INDIA scrape failed:", e)

    print(f"Scraped total {len(all_articles)} articles")
    return all_articles
