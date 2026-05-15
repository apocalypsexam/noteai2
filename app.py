from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""
    topic = ""

    if request.method == "POST":
        topic = request.form["topic"]

        answer = f"""
        <h2>Тема: {topic}</h2>

        <p>
        Это демонстрационная версия сайта.
        AI временно отключен для Render.
        </p>

        <p>
        Позже можно подключить настоящий AI.
        </p>
        """

    return render_template("index.html", answer=answer, topic=topic)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)