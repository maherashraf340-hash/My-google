from flask import Flask, render_template, request
import os

app = Flask(__name__)
AFF_ID = "حط_الايدي_بتاعك_من_نون_هنا" # من noonpartners.com

@app.route("/", methods=["GET", "POST"])
def home():
    query = ""
    results = []
    
    if request.method == "POST":
        query = request.form.get("query")
        if query:
            noon_link = f"https://www.noon.com/egypt-ar/search?q={query}&aff_id={AFF_ID}"
            results = [{
                "title": f"ابحث عن {query} في نون",
                "price": "شوف السعر على نون",
                "link": noon_link
            }]

    return render_template('index.html', query=query, results=results)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
