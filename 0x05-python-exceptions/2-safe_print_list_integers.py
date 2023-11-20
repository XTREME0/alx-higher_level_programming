#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    j = 0
    while x > 0:
        try:
            print(my_list[i], end="")
            i += 1
            j += 1
            x -= 1
        except ValueError:
            i += 1
            continue
        except IndexError:
            break
    print("")
    return j
