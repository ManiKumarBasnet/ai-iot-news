import os
import datetime
from fetch_news import fetch_news

# Output folder
NEWS_DIR = "news"

def generate_html(news_data, date_str):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>🗞️ AI–IoT–Tech Digest – {date_str}</title>
  <link rel="stylesheet" href="../assets/style.css">
</head>
<body>
  <div class="container">
    <h1>🗞️ AI–IoT–Tech News – {date_str}</h1>
"""
    for category, articles in news_data.items():
        html += f"<section><h2>{category}</h2><div class='card-container'>"
        for article in articles:
            html += f"""
            <div class="card">
              <h3>{article['title']}</h3>
              <p>{article['summary']}</p>
              <a href="{article['link']}" target="_blank">Read more</a>
            </div>
            """
        html += "</div></section>"
    
    html += """
    <footer>🛰️ Delivered by your local AI–IoT News Bot 🇧🇹</footer>
  </div>
</body>
</html>"""
    return html

def save_news_page(html, date_str):
    file_path = os.path.join(NEWS_DIR, f"{date_str}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Saved: {file_path}")

def generate_today_news():
    today = datetime.date.today().isoformat()
    news_data = fetch_news()
    html = generate_html(news_data, today)
    save_news_page(html, today)

# Test
if __name__ == "__main__":
    generate_today_news()
