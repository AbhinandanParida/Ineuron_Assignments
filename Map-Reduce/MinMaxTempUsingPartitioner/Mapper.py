#!/usr/bin/env python

import sys

for line in sys.stdin:
        line = line.strip()
        arr = line.split(',')
        datelist=arr[0].split('-')
        year=datelist[-1]
        temp=arr[-1]

        print "%s\t%s" % (year,temp)
