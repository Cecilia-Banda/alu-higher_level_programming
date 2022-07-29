#!/usr/bin/python3
""" Function that finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """ Sort the list """

    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
