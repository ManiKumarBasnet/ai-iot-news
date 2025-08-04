import os
import datetime
from fetch_news import fetch_news
from generate_news_html import generate_html, save_news_page

def build_today_news():
    today = datetime.date.today().isoformat()
    news = fetch_news()
    html = generate_html(news, today)
    save_news_page(html, today)
    print(f"✅ Daily build complete: news/{today}.html")

if __name__ == "__main__":
    build_today_news()
