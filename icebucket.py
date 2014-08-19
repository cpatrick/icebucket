from flask import Flask, render_template
import pymongo
from bson.json_util import dumps
import os

app = Flask(__name__)


@app.route('/data')
def data():
    conn = pymongo.Connection(os.environ['MONGOLAB_URI'])
    db = conn.get_default_database()
    return dumps(list(db['challenges'].find()))


@app.route('/')
def index():
    return render_template('index.html')
