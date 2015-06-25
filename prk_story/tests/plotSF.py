#!/usr/bin/env python
from plotdevice import * 
# import timeit

svg = ximport("svg")
color(mode=RGB, range=255)

paths = svg.parse(open('/Users/karen/pyprojects/prk_story/tests/sf36.svg').read())

# this still renders as solid black, when everything should be base-255?
for path in paths:
    fill(120,76,0,150)

drawpath(path)

export("/Users/karen/pyprojects/prk_story/tests/plotsf2.eps")
# print "time to run: %g" % (timeit.Timer)