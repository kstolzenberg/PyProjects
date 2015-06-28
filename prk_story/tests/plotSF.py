#!/usr/bin/env python
# enoding: utf-8
import time
start = time.time()

import plotdevice

print "time to import: %g" % (time.time()-start)

quit()

svg = pd.ximport("svg")
# pd.color(mode=RGB, range=255)
pd.nofill()


paths = svg.parse(open('/Users/karen/pyprojects/prk_story/tests/sf36.svg').read())

# this still renders as solid black, when everything should be base-255?
for path in paths:
    pd.drawpath(path)

# you need to center both of these around center! this documentation sucks
pd.size(500,500)
pd.export("/Users/karen/pyprojects/prk_story/tests/2.pdf")
