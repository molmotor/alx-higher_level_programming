#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for element in my_list:
        for i in range(x):
            try:
                if my_list[i] == int():
                    print("{:d}".format(my_list[i]))
                    count+= 1
                else:
                    pass
            except(TypeError, ValueError):
                pass

    return count
