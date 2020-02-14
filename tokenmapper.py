#!/usr/bin/env python
import re
import sys

for line in sys.stdin:
    val = line.strip()
    tokens = val.split()
    for token in tokens:
        print("%s\t%s" % (token, 1))
