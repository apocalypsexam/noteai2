from flask import Flask, render_template, request
import os
import ollama

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""
    topic = ""

    if request.method == "POST":
        topic = request.form["topic"]

        prompt = f"""
Ты — умный преподаватель.

Объясни тему подробно и понятно школьнику:

{topic}

Структура:
- Введение
- Основная часть (по пунктам)
- Интересные факты
- Вывод

Пиши красиво, с абзацами.
"""

        response = ollama.chat(
            model="llama3",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        answer = response["message"]["content"]

    return render_template("index.html", answer=answer, topic=topic)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)