#!/usr/bin/python3
def element_at(my_list, idx):

    index = 0
    if idx < 0:
        return None

    for element in my_list:
        if index == idx:
            return (element)
        index += 1
    if idx > index:
        return None
