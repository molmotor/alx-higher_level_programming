#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    total = 0

    for element in my_list:
        if element not in my_list:
            new_list.append(element)
            total += element

    return total
