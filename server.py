from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')   #return "<p>Hello, OLTIIIIII!</p>" mund te bejme kete ose thirrim HTML

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