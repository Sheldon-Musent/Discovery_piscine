#!/usr/bin/env python3

try:
    num = input("Give me a number:")
    num_float = float(num)

    if num_float %1 == 0:
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("Invalid Number!")