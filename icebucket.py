from flask import Flask

app = Flask(__name__, static_url_path='')


@app.route('/data')
def data():
    with open('icebucket.json', 'r') as json_file:
        return json_file.read()


@app.route('/')
@app.route('')
def root():
    return app.send_static_file('index.html')
