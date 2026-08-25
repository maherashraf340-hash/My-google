from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    query = ""
    results = []
    
    if request.method == "POST":
        query = request.form.get("query")
        # بنعمل لينك البحث في نون مصر
        noon_link = f"https://www.noon.com/egypt-ar/search?q={query}"
        results = [{
            "title": f"نتائج البحث عن {query} في نون",
            "price": "اضغط للعرض",
            "link": noon_link,
            "image": "https://z.nooncdn.com/s/app/com/noon/icons/logo-noon.svg"
        }]

    return render_template('index.html', query=query, results=results)from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    query = ""
    results = []
    
    if request.method == "POST":
        query = request.form.get("query")
        # بنعمل لينك البحث في نون مصر
        noon_link = f"https://www.noon.com/egypt-ar/search?q={query}"
        results = [{
            "title": f"نتائج البحث عن {query} في نون",
            "price": "اضغط للعرض",
            "link": noon_link,
            "image": "https://z.nooncdn.com/s/app/com/noon/icons/logo-noon.svg"
        }]

    return render_template('index.html', query=query, results=results)from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    query = ""
    results = []
    
    if request.method == "POST":
        query = request.form.get("query")
        # بنعمل لينك البحث في نون مصر
        noon_link = f"https://www.noon.com/egypt-ar/search?q={query}"
        results = [{
            "title": f"نتائج البحث عن {query} في نون",
            "price": "اضغط للعرض",
            "link": noon_link,
            "image": "https://z.nooncdn.com/s/app/com/noon/icons/logo-noon.svg"
        }]

    return render_template('index.html', query=query, results=results)from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    query = ""
    results = []
    
    if request.method == "POST":
        query = request.form.get("query")
        # بنعمل لينك البحث في نون مصر
        noon_link = f"https://www.noon.com/egypt-ar/search?q={query}"
        results = [{
            "title": f"نتائج البحث عن {query} في نون",
            "price": "اضغط للعرض",
            "link": noon_link,
            "image": "https://z.nooncdn.com/s/app/com/noon/icons/logo-noon.svg"
        }]

    return render_template('index.html', query=query, results=results)from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    query = ""
    results = []
    
    if request.method == "POST":
        query = request.form.get("query")
        # بنعمل لينك البحث في نون مصر
        noon_link = f"https://www.noon.com/egypt-ar/search?q={query}"
        results = [{
            "title": f"نتائج البحث عن {query} في نون",
            "price": "اضغط للعرض",
            "link": noon_link,
            "image": "https://z.nooncdn.com/s/app/com/noon/icons/logo-noon.svg"
        }]

    return render_template('index.html', query=query, results=results)from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    query = ""
    results = []
    
    if request.method == "POST":
        query = request.form.get("query")
        # بنعمل لينك البحث في نون مصر
        noon_link = f"https://www.noon.com/egypt-ar/search?q={query}"
        results = [{
            "title": f"نتائج البحث عن {query} في نون",
            "price": "اضغط للعرض",
            "link": noon_link,
            "image": "https://z.nooncdn.com/s/app/com/noon/icons/logo-noon.svg"
        }]

    return render_template('index.html', query=query, results=results)from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    query = ""
    results = []
    
    if request.method == "POST":
        query = request.form.get("query")
        # بنعمل لينك البحث في نون مصر
        noon_link = f"https://www.noon.com/egypt-ar/search?q={query}"
        results = [{
            "title": f"نتائج البحث عن {query} في نون",
            "price": "اضغط للعرض",
            "link": noon_link,
            "image": "https://z.nooncdn.com/s/app/com/noon/icons/logo-noon.svg"
        }]

    return render_template('index.html', query=query, results=results)from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    query = ""
    results = []
    
    if request.method == "POST":
        query = request.form.get("query")
        # بنعمل لينك البحث في نون مصر
        noon_link = f"https://www.noon.com/egypt-ar/search?q={query}"
        results = [{
            "title": f"نتائج البحث عن {query} في نون",
            "price": "اضغط للعرض",
            "link": noon_link,
            "image": "https://z.nooncdn.com/s/app/com/noon/icons/logo-noon.svg"
        }]

    return render_template('index.html', query=query, results=results)
