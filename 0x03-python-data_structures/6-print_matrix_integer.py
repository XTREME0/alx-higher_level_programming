#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        swtch = 0
        for num in line:
            if swtch:
                print(" ", end="")
            swtch = 1
            print("{} ".format(num), end="")
        print("")
