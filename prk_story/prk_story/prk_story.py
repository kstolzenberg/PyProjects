from flask import Flask 
from flask import render_template

import requests
import json

app = Flask(__name__)
@app.route('/parking')

def hello():
    r = requests.get("https://data.sfgov.org/resource/uupn-yfaw.json")
    data = json.loads(r.text)
    # the data is flowing!
    return data[5]['regcap']


if __name__ == "__main__":
    app.run(debug=True)