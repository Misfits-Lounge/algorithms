#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.system('clear')

#list(mutable, append, insert, pop, sort, reverse, del, index, count, remove)
mylist = range(0,100)
#Tuples(immutable,union, diff, issubset, remove, pop, clear )
myset = {'value1', 4.5, True, 10}
#dictionaries(mutable, keys(), values(), items(), get(key(alt),)
mydict = {'first_key':1, 'second_key': True, 'third_key': [1,2,3,4]}


wordlist = ['cat','dog','rabbit']
letterlist = []

def strip_letters():
    for aword in wordlist:
        for aletter in aword:
            if aletter not in letterlist:
                letterlist.append(aletter)
    print letterlist

#strip_letters()
def list_comp():
    dicto = {}
    [dicto.setdefault(i,word[i]) for word in wordlist for i in range(len(word))]
    print dicto

#list_comp()
def squareroot(n):
    root = n/2    #initial guess will be 1/2 of n
    for k in range(20):
        try :
            root = (1/2)*(root + (n / root))
        except ZeroDivisionError as e:
            pass

    return root

#squareroot(9)


#time complexity O(1)
def fast_solution(n):
    result = n * (n+1) // 2
    print result


#n = raw_input('Enter integer: ')
#fast_solution(int(n))


"""Euclid’s Algorithm states that the greatest common divisor of two integers m
 and n is n if n divides m evenly. However, if n does not divide m evenly, then
 the answer is the greatest common divisor of n and the remainder of m divided by
 n. We will simply provide an iterative implementation here (see ActiveCode 1).
 Note that this implementation of the GCD algorithm only works when the denominator
 is positive. This is acceptable for our fraction class because we have said that a
 negative fraction will be represented by a negative numerator.
"""

def gcd(m,n): #great common denominator
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

#print gcd(10,20)



#Redhat interview question, 
#find the biggest sufix of 2 words, and return it

def get_sufix(x, y):
    suffix = []
    for xchar in xrange(len(x)):
        for ychar in xrange(len(y)):
            if x[xchar] == y[ychar]:
                suffix.append(y[ychar])
    return suffix

print get_sufix('parlament', 'antrenament')
