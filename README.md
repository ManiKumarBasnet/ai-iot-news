# 📡 AI–IoT–News Auto Site

A self-updating static site that delivers daily **AI**, **IoT**, **Embedded**, **Blockchain**, and **Bhutan Tech** news.

Built with **Python + RSS feeds**  
Hosted via **GitHub Pages**  
100% **free**, **automated**, and **customizable**

---

## 🧱 Folder Structure

| Folder                  | Purpose                                                |
|-------------------------|--------------------------------------------------------|
| `news/`                 | Auto-generated daily HTML news files                   |
| `assets/`               | CSS/JS styling and scripts                             |
| `templates/`            | Reusable HTML layout and components                    |
| `pages/`                | Extra pages like About, Donate, Games                  |
| `.github/workflows/`    | GitHub Actions config for daily automation             |

---

## 🚀 How to Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Then build today's news:

```bash
python build.py
```

This will:
* 📰 Fetch and categorize news from all sources
* 🛠️ Generate a fresh HTML page inside `/news/`
* 🏠 Update your homepage with the new content

## 🌐 Host on GitHub Pages

1. Create a public GitHub repo (e.g. `ai-iot-news`)
2. Push your project code
3. Go to **Settings → Pages**
4. Set **Source** to `main`, folder to `/ (root)`

📎 Your site will be live at:

```
https://yourusername.github.io/ai-iot-news/news/YYYY-MM-DD.html
```

## 🔄 Automation (No Zapier, No Cost)

This project includes a GitHub Actions workflow that:
* 🕒 Runs daily at **5:00 UTC** (≈ 10:30 AM Bhutan time)
* 🔁 Builds new content and pushes it live automatically
* 🛠️ No manual trigger needed

You can also manually run it via GitHub's "Run Workflow" button.

## 🧩 Extending the Project

You can easily extend with:
* 🌗 **Dark mode** toggle in layout
* 🕹️ **Games page** for tech learning or engagement
* 💰 **AdSense / affiliate links** in sidebar or footer
* 📬 **Newsletter integration** via Buttondown, Substack or Mailchimp
* 🗃️ **Offline archive viewer** to browse past issues

To add more categories: Edit `RSS_FEEDS` inside `fetch_news.py`.

## 🧪 Technologies Used

* Python 3.11+
* `feedparser` and `BeautifulSoup`
* Jinja2 templates (optional)
* GitHub Pages + GitHub Actions

## 🧠 Credits

Made with ❤️ in Bhutan 🇧🇹 By an embedded engineer who loves automation, microcontrollers, and tech that empowers.

## 📅 Live Example

Check the latest digest: 👉 https://yourusername.github.io/ai-iot-news/news/YYYY-MM-DD.html

---

### ✅ Next Step:

1. Replace `yourusername` with your GitHub username
2. Save it as `README.md`
3. Run:

```bash
git add README.md
git commit -m "📝 Complete README with full structure and deployment info"
git push
```