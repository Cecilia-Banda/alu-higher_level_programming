#!/usr/bin/python3
def no_c(my_string):

     convertList = list(my_string)
    index = 0
    editedString = ""

    if (len(my_string)) == 0:
        return my_string

    new_string = convertList[:]

    for elements in new_string[:]:
        if elements == 'c' or elements == 'C':
            del(new_string[index])
            index -= 1
        index += 1
    return (editedString.join(new_string))
