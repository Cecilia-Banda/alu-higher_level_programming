#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

    index = 0

    if (len(my_list) == 0):
        return my_list

    if idx == (len(my_list)):
        return my_list

    if idx < 0:
        return my_list

    for elem in my_list:
        if index == idx:
            my_list[index] = element
            return my_list
        index += 1

    if idx > index:
        return my_list
