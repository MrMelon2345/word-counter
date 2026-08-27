import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    words = None

    if request.method == "POST":
        text = request.form["text"]

        # Remove text inside quotation marks
        text = re.sub(r'“[^"]*”', '', text)

        text = re.sub(r'[.,!?;:]', '', text)

        # Count the words
        words = len(text.split())

    return render_template("index.html", words=words)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)