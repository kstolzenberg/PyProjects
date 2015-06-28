#!/usr/bin/env python
import time

start = time.time()


from plotdevice import *

svg = ximport("svg")
color(mode=RGB, range=255)
nofill()


paths = svg.parse(open('/Users/karen/pyprojects/prk_story/tests/sf36.svg').read())

# this still renders as solid black, when everything should be base-255?
for path in paths:
    drawpath(path)

# you need to center both of these around center! this documentation sucks
size(500,500)
export("/Users/karen/pyprojects/prk_story/tests/2.pdf")
print "time to run: %g" % (time.time()-start)