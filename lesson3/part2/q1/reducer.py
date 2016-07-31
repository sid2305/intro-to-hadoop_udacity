#!/usr/bin/python


import sys

count = 0
oldKey = None


for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisCount = data

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", count
        oldKey = thisKey;
        count = 0

    oldKey = thisKey
    count += int(thisCount)

if oldKey != None:
    print oldKey, "\t", count
