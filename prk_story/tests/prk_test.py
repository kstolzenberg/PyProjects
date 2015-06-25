import requests
import json

#gets all the data
r = requests.get("https://data.sfgov.org/resource/uupn-yfaw.json") # these are offstreet from 2011
p = requests.get("https://data.sfgov.org/resource/3gg2-z57m.json") # these are on-street from 2008 - onward

#parse json into python objects
data_off = json.loads(r.text)
data_on = json.loads(p.text)

# sub lists of just the data we care about
reg_stallct = []
valet_stallct = []
street_sply = []

# function to grab specific data from stream and store in a new list. keys are column headers.
def isolate(data_stream, new_list, key):
    for i in range(len(data_stream)):
        new_list.append(float(data_stream[i][key]))

isolate(data_off, reg_stallct, 'regcap')
isolate(data_off, valet_stallct, 'valetcap')
isolate(data_on, street_sply,'prkng_sply')

total_stallct = sum(reg_stallct) + sum(valet_stallct) + sum(street_sply)
total_prk_sf = total_stallct * (162) # 9'* 18' avg prk spot = 162 sq.ft // assumes all stalls the same size
# SF Planning 154: min offstreet size = 8x18=144sf. ADA:9x18  Onstreet:20*8
total_prk_area = total_prk_sf / 27878400 # 1sq mile is 27878400 sq ft
sf_area = 46.87 # sq miles per census bureau // you could subtract out remaining area of streets? not sure how that would overlap?
prk_ratio = (total_prk_area / sf_area)

print "total stall ct: %g" % total_stallct
print "total square miles of parking: %g" % total_prk_area
print "ratio of parking to SF: %g \n rats thats not very high" % prk_ratio

# doesn't even include required parking for businesses or residences
