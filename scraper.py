import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}


def scrape_website(url):
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        paragraphs = [p.get_text() for p in soup.find_all("p")]
        return " ".join(paragraphs[:30])
    except:
        return ""


def scrape_reddit_for_competitor(name):
    url = "https://www.reddit.com/r/projectmanagement/hot.json?limit=20"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        res = requests.get(url, headers=headers)
        data = res.json()

        posts = []
        for p in data["data"]["children"]:
            title = p["data"]["title"]
            if name.lower() in title.lower():
                posts.append(title)

        return posts[:5]
    except:
        return []


def scrape_capterra_reviews(url):
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        reviews = []
        for div in soup.find_all("div"):
            text = div.get_text(strip=True)
            if len(text) > 100 and "Pros" in text:
                reviews.append(text)

        return reviews[:5]
    except:
        return []


def extract_pricing(text):
    pricing_keywords = ["$", "price", "per user", "month"]
    lines = text.split(".")
    pricing_info = []

    for line in lines:
        if any(k.lower() in line.lower() for k in pricing_keywords):
            pricing_info.append(line.strip())

    return pricing_info[:5]


def get_competitor_data():
    competitors = {
        "Notion": {
            "site": "https://www.notion.so/product",
            "capterra": "https://www.capterra.com/p/164979/Notion/"
        },
        "Asana": {
            "site": "https://asana.com/product",
            "capterra": "https://www.capterra.com/p/143452/Asana/"
        },
        "ClickUp": {
            "site": "https://clickup.com/features",
            "capterra": "https://www.capterra.com/p/183565/ClickUp/"
        },
        "Monday": {
            "site": "https://monday.com/product",
            "capterra": "https://www.capterra.com/p/147657/monday-com/"
        }
    }

    data = {}

    for name, urls in competitors.items():
        print(f"Scraping {name}...")

        website_text = scrape_website(urls["site"])
        reddit = scrape_reddit_for_competitor(name)
        reviews = scrape_capterra_reviews(urls["capterra"])
        pricing = extract_pricing(website_text)

        data[name] = {
            "website": website_text,
            "reddit": reddit,
            "reviews": reviews,
            "pricing": pricing
        }

    return data