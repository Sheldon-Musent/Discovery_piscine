#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    lowercase = sys.argv[1].lower()
    print(lowercase)
else:
    print("none")