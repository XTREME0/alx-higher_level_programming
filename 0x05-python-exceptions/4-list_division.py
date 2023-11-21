#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    result = []
    while list_length > 0:
        try:
            result.append(my_list_1[i] / my_list_2[i])
            list_length -= 1
            i += 1
        except TypeError:
            print("wrong type")
            result.append(0)
            list_length -= 1
            i += 1
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
            list_length -= 1
            i += 1
        except IndexError:
            result.append(0)
            print("out of range")
            break
        finally:
            True
    return result
