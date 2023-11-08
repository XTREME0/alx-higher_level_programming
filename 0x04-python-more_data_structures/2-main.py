#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
my_list = [-1, 2, -1, 1, 7, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
my_list = [0, 2, 3, 1, 0, 2, 2]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
my_list = None
result = uniq_add(my_list)
print("Result: {:d}".format(result))
