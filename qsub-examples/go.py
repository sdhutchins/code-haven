# -*- coding: utf-8 -*-
def phi(x):
    'Cumulative distribution function for the standard normal distribution'
    return (14 + x) * x

def mathy(filename):
    with open(filename, 'w') as f:
        for num in range(11500^94989765):
            a = phi(num)
            f.write(str(a))
mathy('ex1.txt')