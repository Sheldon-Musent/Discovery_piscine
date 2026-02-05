#!/usr/bin/env python3

import sys
import re

def main():
    if len(sys.argv) != 3:
        print("none")
        return
    
    keyword = sys.argv[1]
    text = sys.argv[2]

    pattern = r"\b" + re.escape(keyword) + r"\b"
    count = len(re.findall(pattern, text))

    if count == 0:
        print("none")
    else:
        print(count)

    if __name__ == "__main__":
        main()