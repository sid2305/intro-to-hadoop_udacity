#!/usr/bin/python

import sys

max_Sale = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    thisSale = float(thisSale)
    if thisSale > max_Sale:
        max_Sale = thisSale

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", max_Sale
        oldKey = thisKey;
        max_Sale = 0

    oldKey = thisKey

if oldKey != None:
    print oldKey, "\t", max_Sale
