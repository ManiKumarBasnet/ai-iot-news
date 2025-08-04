# 📡 AI–IoT–News Auto Site

A self-updating static site that delivers daily AI, IoT, Embedded, Blockchain, and Bhutan tech news. Built with Python + RSS feeds. 100% free, local, and extendable.

---

## 🧱 Folder Structure

| Folder          | Purpose                                  |
|-----------------|------------------------------------------|
| `news/`         | Auto-generated daily HTML news files     |
| `assets/`       | CSS/JS styling and scripts               |
| `templates/`    | Reusable HTML layout and components      |
| `pages/`        | Extra pages like About, Donate, Games    |

---

## 🚀 How to Run

```bash
python build.py
This will:

Fetch news from RSS

Generate HTML for today

Update the homepage with today's news

🌐 Deployment
Use GitHub Pages to host for free:

Push to a GitHub repo

Go to Settings → Pages → Set source to main and folder to /root

URL will be something like:
https://yourusername.github.io/ai-iot-news/news/2025-08-04.html

🔮 Features Roadmap
 Dark mode toggle

 Games page with educational tools

 Ads/affiliate integration

 Offline news archive viewer

 Email/newsletter support