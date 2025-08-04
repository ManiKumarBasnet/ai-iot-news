import feedparser
from bs4 import BeautifulSoup

# Define categories and RSS sources
RSS_FEEDS = {
    "AI": [
        "https://www.ainewswire.com/feed/",
        "https://venturebeat.com/category/ai/feed/",
    ],
    "IoT": [
        "https://iotbusinessnews.com/feed/",
        "https://www.iotworldtoday.com/feed/",
    ],
    "Embedded": [
        "https://embeddedcomputing.com/rss",
        "https://www.cnx-software.com/feed/",
    ],
    "Blockchain": [
        "https://cryptobriefing.com/feed/",
        "https://cointelegraph.com/rss",
    ],
    "Latest Tech": [
        "https://techcrunch.com/feed/",
        "https://thenextweb.com/feed/",
    ],
    "Bhutan": [
        "https://www.kuenselonline.com/feed/",
        "https://thebhutanese.bt/feed/",
    ],
}

def clean_html(html):
    """Remove HTML tags and decode entities."""
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()

def fetch_news():
    """Returns a dictionary of news headlines by category."""
    news = {}
    for category, urls in RSS_FEEDS.items():
        news[category] = []
        for url in urls:
            feed = feedparser.parse(url)
            for entry in feed.entries[:2]:  # limit to 2 per source
                title = entry.title
                summary = clean_html(entry.get("summary", "")[:250]) + "..."
                link = entry.link
                news[category].append({
                    "title": title,
                    "summary": summary,
                    "link": link
                })
    return news

# Run for testing
if __name__ == "__main__":
    data = fetch_news()
    for cat, articles in data.items():
        print(f"\n=== {cat} ===")
        for a in articles:
            print(f"- {a['title']}\n  {a['summary']}\n  {a['link']}\n")
