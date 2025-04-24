from flask import Flask, render_template, request
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are a helpful assistant for Erolt Laci's personal portfolio site. Answer questions about him, his services, and projects in Python, AI, and automation. If you're unsure, ask them to check the page or contact him directly."},
                {"role": "user", "content": user_input}
            ]

        )
        response_text = response.choices[0].message.content
    return render_template("index.html", response=response_text)

   #return "<p>Hello, OLTIIIIII!</p>" mund te bejme kete ose thirrim HTML

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/ml-ai')
def ml_ai():
    return render_template('ml-ai.html')

@app.route('/web-tools')
def web_tools():
    return render_template('web-tools.html')





import os
from flask import send_from_directory

@app.route('/skull.ico') # per ti vu 1 ikone website ne krye, duhet konfiguru edhe tek HTML
def skull():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'skull.ico', mimetype='image/vnd.microsoft.icon')

# per tu fut tek venv tek cmd shkruj kete: "venv\Scripts\activate", pastaj thirr flask ne cmd: "flask --app server run"
# per te aktivizu DEBUG : "flask --app server run --debug"

if __name__ == "__main__":
    app.run(debug=True)
