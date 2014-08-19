from flask import Flask

app = Flask(__name__, static_url_path='')


@app.route('/data')
def data():
    with open('icebucket.json', 'r') as json_file:
        return json_file.read()


@app.route('/')
def root():
    with open('index.html', 'r') as index_file:
        return index_file.read()
