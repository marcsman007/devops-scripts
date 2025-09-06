#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("Usage: python log-parser.py /path/to/logfile keyword")
    sys.exit(1)

logfile = sys.argv[1]
keyword = sys.argv[2]

with open(logfile, 'r') as file:
    for line in file:
        if keyword.lower() in line.lower():
            print(line.strip())
