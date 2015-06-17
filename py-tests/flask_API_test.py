#use Flask to send dynamic API info to the browser

from flask import Flask
app = Flask(__name__)

import requests
import json

# this is the path after the local ip
@app.route("/vimeo")


def hello():
    # get data from external API URL & read in python
    r = requests.get("https://vimeo.com/api/v2/channel/staffpicks/videos.json")
    # r.text is a method to access just the text of the request
    # convert r.text to python and store in list 'data'
    data = json.loads(r.text)

    # make a new empty list to store our new title list from JSON bc we only want some of the data
    all_videos = []

    # loop through the JSON variable and find the titles
    for i in range(len(data)):
        all_videos.append(data[i]['title']) # there were lists and dictionaries in the json data...access each differently

    # make string for html formatting // this is really just string formatting!
    html_str = "<b>Vimeo's top picks:</b>"

    # for each value in all_videos, add to html_str an html break and each individual list value
    for movie in all_videos:
        html_str += ("<br> %s" % movie)

    # return is one final event - all the code stops there! = return our complete string.
    return html_str


if __name__ == "__main__":
    app.run(debug=True)

# will run on local ip: http://127.0.0.1:5000/vimeo
