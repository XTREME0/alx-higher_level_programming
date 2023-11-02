#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv)
    if l == 2:
        print("{} argument:".format(1))
    elif l == 1:
        print("{} arguments.".format(0))
    else:
        print("{} arguments:".format(l-1))
    if l > 1:
        for i in range(1, l):
            print("{}: {}".format(i, sys.argv[i]))
