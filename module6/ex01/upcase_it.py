#!/usr/bin/env python3

import sys

if len(sys.argv) >1:
    uppercase = sys.argv[1].upper()
    print(uppercase)
else:
    print("none")