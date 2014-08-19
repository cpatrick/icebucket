from flask import Flask, render_template

app = Flask(__name__)


@app.route('/data')
def data():
    with open('icebucket.json', 'r') as json_file:
        return json_file.read()


@app.route('/')
def index():
    return render_template('index.html')
