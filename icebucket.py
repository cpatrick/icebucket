from flask import Flask
import os

app = Flask(__name__,
            static_url_path='',
            static_folder=os.path.dirname(os.path.realpath(__file__)))


@app.route('/data')
def data():
    with open('icebucket.json', 'r') as json_file:
        return json_file.read()


@app.route('/')
def root():
    with open('index.html', 'r') as index_file:
        return index_file.read()


@app.route('/js/<path:filename>')
def send_js(filename):
    return app.send_from_directory('js', filename)


@app.route('/css/<path:filename>')
def send_css(filename):
    return app.send_from_directory('css', filename)


@app.route('/img/<path:filename>')
def send_img(filename):
    return app.send_from_directory('img', filename)


@app.route('/fonts/<path:filename>')
def send_fonts(filename):
    return app.send_from_directory('fonts', filename)
