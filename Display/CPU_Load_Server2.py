#!/usr/bin/env python

import serial
import time

port = serial.Serial('/dev/ttyUSB0', 57600)

old = None
old1 = None
old2 = None
old3 = None
old4 = None

while True:
    with open('/proc/stat') as stat:
        new = map(float, stat.readline().strip().split()[1:])
        processor1 = map(float, stat.readline().strip().split()[1:])
        processor2 = map(float, stat.readline().strip().split()[1:])
        processor3 = map(float, stat.readline().strip().split()[1:])
        processor4 = map(float, stat.readline().strip().split()[1:])

    if old is not None:
        diff = [n - o for n, o in zip(new, old)]
        idle = diff[3] / sum(diff)
        d1 = [n - o for n, o in zip(processor1, old1)]
        i1 = d1[3] / sum(d1)
        d2 = [n - o for n, o in zip(processor2, old2)]
        i2 = d2[3] / sum(d2)
        d3 = [n - o for n, o in zip(processor3, old3)]
        i3 = d3[3] / sum(3)
        d4 = [n - o for n, o in zip(processor4, old4)]
        i4 = d4[3] / sum(d4)

        port.write("CPU Load %2.0f" %(100 * (1 - idle)))
        port.write(100 * (1-i1),
        port.write(100 * (1-i2),
        port.write(100 * (1-i3),
        port.write(100 * (1-i4),
        
    old = new
    old1 = processor1
    old2 = processor2
    old3 = processor3
    old4 = processor4

    time.sleep(0.25)


