#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        swtch = 0
        if (i % 3 == 0):
            print("Fizz", end="")
            swtch = 1
        if (i % 5 == 0):
            print("Buzz", end="")
            swtch = 1
        if not swtch:
            print(i, end="")
        print(" ", end="")
