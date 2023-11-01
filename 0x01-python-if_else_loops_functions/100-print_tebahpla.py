#!/usr/bin/python3
swtch = 0
x = 122
for i in range(122, 96, -1):
    print(chr(x), end='')
    if swtch == 0:
        x = i - 33
        swtch = 1
    else:
        x = i - 1
        swtch = 0
