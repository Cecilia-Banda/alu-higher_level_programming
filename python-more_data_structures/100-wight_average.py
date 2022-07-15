#!/usr/bin/python3
def weight_average(my_list=[]):
    points = 0
    total = 0
    if my_list:
        tup = ()
        for tup in my_list:
            points += (tup[0] * tup[1])
            total += tup[1]
        return points / total
    return 0
