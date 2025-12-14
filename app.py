from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    search_query = None
    if request.method == "POST":
        search_query = request.form.get("query")
    return render_template("index.html", search_query=search_query)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

