from flask import Flask, render_template, request, jsonify
import requests
import google.generativeai as genai # للـ AI

app = Flask(__name__)

# حط مفتاح الـ API بتاعك هنا من https://aistudio.google.com
genai.configure(api_key="حط_المفتاح_بتاعك_هنا")
model = genai.GenerativeModel('gemini-1.5-flash')

def search_products(query):
    # دي مكان ما هتربط API حقيقي. دلوقتي بنرجع داتا وهمية
    return [
        {"title": f"لابتوب {query} - سوق", "price": "14500 جنيه", "link": "https://souq.com"},
        {"title": f"لابتوب {query} - نون", "price": "15200 جنيه", "link": "https://noon.com"},
        {"title": f"لابتوب {query} - أمازون", "price": "13999 جنيه", "link": "https://amazon.eg"}
    ]

def summarize_with_ai(query, results):
    prompt = f"المستخدم بحث عن: {query}. دي النتائج: {results}. لخصله أرخص واحد وأحسن واحد في سطرين بالعربي"
    response = model.generate_content(prompt)
    return response.text

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    summary = ""
    if request.method == "POST":
        query = request.form["query"]
        results = search_products(query)
        summary = summarize_with_ai(query, results)
    return render_template("index.html", results=results, summary=summary, query=query if request.method == "POST" else "")

if __name__ == "__main__":
    app.run(debug=True)