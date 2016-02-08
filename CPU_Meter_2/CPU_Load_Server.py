#!/usr/bin/env python

import serial
import time

port = serial.Serial('/dev/ttyUSB0', 57600)

old = None
while True:
    with open('/proc/stat') as stat:
        new = map(float, stat.readline().strip().split()[1:])
    if old is not None:
        diff = [n - o for n, o in zip(new, old)]
        idle = diff[3] / sum(diff)
        port.write(chr(int(180 * (1 - idle))))
   
    old = new
    time.sleep(0.25)


