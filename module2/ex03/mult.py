#!/usr/bin/env python3

x = int(input ("Enter the first number:\n"))
y = int(input ("Enter the second number:\n"))

z = x * y
print(f"{x} X {y} = {z}")

if z > 0:
    print("The results is positive.")

elif z == 0:
    print("The results is positive and negative.")

else:
    print("The result is negative.")