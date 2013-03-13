#!/usr/bin/env python

# This script takes in a single image file and makes a call to imagemagick
# to create smaller versions sized appropriately for different iOS devices,
# assuming the input graphic is optimized for an iPad Retina.

# Created by Kevin Jones <kevin.chris.jones@gmail.com> on 12 March 2013.

import sys
import os
from subprocess import call

filename = sys.argv[1]

def resizeImage(scaleString, deviceSuffix):
    compoundFilename = basefilename + deviceSuffix + ext
    call(["convert", filename, "-resize", scaleString, compoundFilename])

def makeScaledImages(filename):
    basefilename, ext = os.path.splitext(filename)

    # TODO: break off the -ipadhd from the filename if it's there

    def resizeImage(scaleString, deviceSuffix):
        compoundFilename = basefilename + deviceSuffix + ext
        call(["convert", filename, "-resize", scaleString, compoundFilename])

    call(["cp", filename, filename + ".backup"])
    resizeImage("100%", "-ipadhd")
    resizeImage("50%", "-hd")
    resizeImage("25%", "")

for arg in sys.argv:
    if arg == sys.argv[0]:
        pass

    makeScaledImages(arg)
