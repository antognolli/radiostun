#!/usr/bin/env python

# Playing a radio stream with EFL (Emotion)

import ecore
import ecore.evas
from emotion import Emotion

DSIZE = 320, 240
FILENAME = 'http://relay5.slayradio.org:8000/'

ee = ecore.evas.new()
ee.size = DSIZE
ee.show()

canvas = ee.evas
em = Emotion(canvas, module_filename='generic')
em.file = FILENAME
em.size = DSIZE
em.play = True
em.show()

if __name__ == '__main__':
    m = ecore.MainLoop()
    m.begin()
