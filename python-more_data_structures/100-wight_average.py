#!/usr/bin/python3

   
def weight_average(my_list=[]):
    if len(my_list) <= 0:
        return 0
    else:
        total_weight = 0
        number_of = 0
        for temp in my_list:
            total_weight += (temp[0] * temp[1])
            number_of += temp[1]
        average = total_weight/number_of
        return average
