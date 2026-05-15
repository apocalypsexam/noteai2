from flask import Flask, render_template, request
import requests
import os
import markdown

app = Flask(__name__)

API_KEY = os.getenv("OPENROUTER_API_KEY")


@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""
    topic = ""

    if request.method == "POST":

        topic = request.form["topic"]

        prompt = f"""
Ты умный преподаватель.

Подробно и понятно объясни тему:

{topic}

Структура:
- Введение
- Основная часть
- Интересные факты
- Вывод

Используй:
- заголовки
- списки
- красивое оформление
"""

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek/deepseek-chat",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
        )

        data = response.json()

        print(data)

        if "choices" in data:

            raw_answer = data["choices"][0]["message"]["content"]

            answer = markdown.markdown(raw_answer)

        else:

            answer = f"""
            <h2>Ошибка AI</h2>
            <p>{data}</p>
            """

    return render_template(
        "index.html",
        answer=answer,
        topic=topic
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)