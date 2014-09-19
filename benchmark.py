#!/usr/bin/env python

import time

dataset = 100000000


def n_total(n):
    start = time.time()
    thesum = 0
    for i in range(1, n+1):
        thesum = thesum + i
    end = time.time()
    return thesum, end-start


def n_total2(n):
    return (n*(n+1)) / 2


print 'The O(n)', n_total(dataset)
print 'The O(log)', n_total2(dataset)




