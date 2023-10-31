#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = (number > 0) * int(str(number)[-1]) or - int(str(number)[-1])
print(number)
print(n)
if (n > 5):
    print(f"Last digit of {number} is {n} and is greater than 5")
elif (n < 6 and n != 0):
    print(f"Last digit of {number} is {n} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {n} and is 0")
