#!/usr/bin/env python

import serial
import time

port = serial.Serial('/dev/ttyUSB0', 57600)

old = None
olda = None
oldb = None
oldc = None
oldd = None

while True:
    with open('/proc/stat') as stat:
        new = map(float, stat.readline().strip().split()[1:])
    if old is not None:
        diff = [n - o for n, o in zip(new, old)]
        idle = diff[3] / sum(diff)
        port.write(str(int(100 * (1 - idle))).rjust(3))
    old = new

    with open('/proc/stat') as stat:
        newa = map(float, stat.readline().strip().split()[1:])
        newa = map(float, stat.readline().strip().split()[1:])
    if olda is not None:
        diffa = [n - o for n, o in zip(newa, olda)]
        idlea = diffa[3] / sum(diffa)
        port.write(str(int(100 * (1 - idlea))).rjust(3))
    olda = newa

    with open('/proc/stat') as stat:
        newb = map(float, stat.readline().strip().split()[1:])
        newb = map(float, stat.readline().strip().split()[1:])
        newb = map(float, stat.readline().strip().split()[1:])
    if oldb is not None:
        diffb = [n - o for n, o in zip(newb, oldb)]
        idleb = diffb[3] / sum(diffb)
        port.write(str(int(100 * (1 - idleb))).rjust(3))
    oldb = newb

    with open('/proc/stat') as stat:
        newc = map(float, stat.readline().strip().split()[1:])
        newc = map(float, stat.readline().strip().split()[1:])
        newc = map(float, stat.readline().strip().split()[1:])
        newc = map(float, stat.readline().strip().split()[1:])
    if oldc is not None:
        diffc = [n - o for n, o in zip(newc, oldc)]
        idlec = diffc[3] / sum(diffc)
        port.write(str(int(100 * (1 - idlec))).rjust(3))
    oldc = newc

    with open('/proc/stat') as stat:
        newd = map(float, stat.readline().strip().split()[1:])
        newd = map(float, stat.readline().strip().split()[1:])
        newd = map(float, stat.readline().strip().split()[1:])
        newd = map(float, stat.readline().strip().split()[1:])
        newd = map(float, stat.readline().strip().split()[1:])
    if oldd is not None:
        diffd = [n - o for n, o in zip(newd, oldd)]
        idled = diffd[3] / sum(diffd)
        port.write(str(int(100 * (1 - idled))).rjust(3))
    oldd = newd

    time.sleep(1)


