from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

app = Flask(__name__)
AFF_ID = "partner-12345" # غير ده بال ID بتاعك

def get_noon_results(query):
    results = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    search_url = f"https://www.noon.com/egypt-ar/search?q={urllib.parse.quote(query)}"
    
    try:
        r = requests.get(search_url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        products = soup.select('div.productContainer')[:5] 
        
        for p in products:
            title_tag = p.select_one('div.title')
            price_tag = p.select_one('strong.amount')
            img_tag = p.select_one('img')
            link_tag = p.select_one('a')
            
            if title_tag and price_tag and link_tag:
                title = title_tag.text.strip()
                price = price_tag.text.strip() + " جنيه"
                img = "https:" + img_tag['data-src'] if img_tag else ""
                link = "https://www.noon.com" + link_tag['href'] + f"&aff_id={AFF_ID}"
                results.append({"title": title, "price": price, "img": img, "link": link})
    except Exception as e:
        print(e)
    return results

@app.route("/", methods=["GET", "POST"])
def home():
    query = ""
    results = []
    if request.method == "POST":
        query = request.form.get("query")
        if query:
            results = get_noon_results(query)
    return render_template('index.html', query=query, results=results)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
