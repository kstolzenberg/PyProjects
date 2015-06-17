# references
    # http://www.pythonforbeginners.com/python-on-the-web/how-to-use-the-vimeo-api-in-python/
    # https://developer.vimeo.com/apis/simple#video-response

# requests gets info from HTML key. JSON parses data into Python
import requests
import json

# with the simple API...the URL defines the type of data that you get back!...read the site's documentation for more info!
r = requests.get("https://vimeo.com/api/v2/channel/staffpicks/videos.json")
r.text
data = json.loads(r.text)

# how do you access specific parts of the json?
    # first check the data structure of the output - print type(data)
    # lists can't use keys - they use indexes: data[1]
    # dictionaries can use keys: data['key']
    # this data was a list of dictionaries = step down a level!!!

print "test to access one title: %s \n" % (data[1]['title'])

# now step through all of the data. get the list length, iterate through and add each title to a list. print list!!
# len(data) should be 20 bc of 'simple' API limit

for i in range(len(data)):
    print (data[i]['title'])
