import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import quote
from pathlib import Path

# Search keywords
keywords = [
    "stray dog Bangladesh",
    "street dog Bangladesh",
    "free roaming dog Bangladesh",
    "dog killed Bangladesh",
    "dog poisoning Bangladesh",
    "dog abuse Bangladesh",
    "animal abuse Bangladesh",
    "animal cruelty Bangladesh",
    "animal rights Bangladesh",
    "dog rescue Bangladesh",
    "cat rescue Bangladesh",
    "stray cat Bangladesh",
    "cat killed Bangladesh",
    "dog attack Bangladesh",
    "dog bite Bangladesh",
    "rabies Bangladesh dog",
    "dog vaccination Bangladesh",
    "stray dog relocation Bangladesh",
    "animal welfare Bangladesh",
    "dog lovers Bangladesh"
]
news_data = []

for keyword in keywords:
    query = quote(keyword)
    url = f"https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "xml")

    items = soup.find_all("item")

    for item in items:
        title = item.title.get_text(strip=True) if item.title else "No Title"
        link = item.link.get_text(strip=True) if item.link else "No Link"
        pub_date = item.pubDate.get_text(strip=True) if item.pubDate else "No Date"
        source = item.source.get_text(strip=True) if item.source else "Google News"

        news_data.append({
            "keyword": keyword,
            "title": title,
            "source": source,
            "link": link,
            "date": pub_date
        })

df = pd.DataFrame(news_data)

# Remove duplicates
df = df.drop_duplicates(subset=["title", "link"])

# Create data folder if not exists
Path("data").mkdir(exist_ok=True)

# Save CSV
df.to_csv("data/raw_news.csv", index=False, encoding="utf-8-sig")

print(df.head(10))
print("\nTotal articles collected:", len(df))
print("Scraping completed successfully!")