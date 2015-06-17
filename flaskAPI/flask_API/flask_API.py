# use Flask to send dynamic API info to the browser
# now we want to add templating and static files
import datetime

from flask import Flask
from flask import render_template

app = Flask(__name__)

import requests
import json

# this is the path after the local ip: http://127.0.0.1:5000/vimeo
@app.route("/vimeo")


def hello():
    # grab today's date
    now = datetime.date.today()

    # get data from external API URL & read in python
    r = requests.get("https://vimeo.com/api/v2/channel/staffpicks/videos.json")
    data = json.loads(r.text)

    # make a new empty list to store our new title list from JSON bc we only want some of the data
    all_videos = []

    # loop through the JSON variable to find titles, append to list
    for i in range(len(data)):
        all_videos.append(data[i]['title'])

    # we can iterate through the list in html with jinja! no need to string format here. browser is fine with unicode.
    # this is where we connect templates and template variables
    return render_template('layout.html', all_videos = all_videos, now = now)


if __name__ == "__main__":
    app.run(debug=True)

