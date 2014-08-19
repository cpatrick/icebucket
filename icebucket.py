from flask import Flask
import os

app = Flask(__name__,
            static_url_path='/',
            static_folder=os.path.dirname(os.path.realpath(__file__)))


@app.route('/data')
def data():
    with open('icebucket.json', 'r') as json_file:
        return json_file.read()
