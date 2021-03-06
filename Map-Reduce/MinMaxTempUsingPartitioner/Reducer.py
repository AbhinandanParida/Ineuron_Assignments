#This is for calculating the max for 1990 year and min for 1991 year
#!/usr/bin/env python
import sys

(last_max_key,max_val)=(None,0)
(last_min_key,min_val)=(None,-1)


for line in sys.stdin:
        (key,val)=line.strip().split("\t")

        if key == '1990':
                (last_max_key,max_val)=(key,max(max_val,float(val)))
        elif key == '1991':
                if min_val == -1:
                        min_val = float(val)
                (last_min_key,min_val)=(key,min(min_val,float(val)))

if last_max_key and max_val !=0:
        print "%s\t%s" % (last_max_key,max_val)
if last_min_key and min_val != -1:
        print "%s\t%s" % (last_min_key,min_val)
