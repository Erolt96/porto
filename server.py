from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')   #return "<p>Hello, OLTIIIIII!</p>" mund te bejme kete ose thirrim HTML

@app.route('/elements.html')
def elements():
    return render_template('elements.html')

@app.route('/left-sidebar.html')
def left_sidebar():
    return render_template('left-sidebar.html')

@app.route('/right-sidebar')
def right_sidebar():
    return render_template('right-sidebar.html')





import os
from flask import send_from_directory

@app.route('/skull.ico') # per ti vu 1 ikone website ne krye, duhet konfiguru edhe tek HTML
def skull():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'skull.ico', mimetype='image/vnd.microsoft.icon')

# per tu fut tek venv tek cmd shkruj kete: "venv\Scripts\activate", pastaj thirr flask ne cmd: "flask --app server run"
# per te aktivizu DEBUG : "flask --app server run --debug"