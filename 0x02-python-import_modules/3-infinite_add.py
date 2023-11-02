#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = 0
    skip = 1
    for n in sys.argv:
        if skip:
            skip = 0
            continue
        x += int(n)
print("{}".format(x))
