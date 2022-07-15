#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_len = len(tuple_a)
    b_len = len(tuple_b)
    sum_t = []
    x = []
    y = []
    if a_len >= 2 and b_len >= 2:
        sum_t.append(tuple_a[0] + tuple_b[0])
        sum_t.append(tuple_a[1] + tuple_b[1])
        x = tuple(sum_t)
        return x
    if a_len < 2 or b_len < 2:
        if a_len < 1:
            y = list(tuple_a)
            y.append(0)
            y.append(0)
        if b_len < 1:
            x = list(tuple_b)
            x.append(0)
            x.append(0)
        if a_len == 1:
            y = list(tuple_a)
            y.append(0)
        if b_len == 1:
            x = list(tuple_b)
            x.append(0)
        if b_len >= 2:
            x = list(tuple_b)
        if a_len >= 2:
            y = list(tuple_a)

        sum_t.append(y[0] + x[0])
        sum_t.append(y[1] + x[1])
        x = tuple(sum_t)
        return x
