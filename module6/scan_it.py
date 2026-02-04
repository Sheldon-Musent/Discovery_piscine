#!/usr/bin/env python3

import sys
import re

sys.argv
result = re.findall(r'\bP\w+', sys.argv)
print(result)
