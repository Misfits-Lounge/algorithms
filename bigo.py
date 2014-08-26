#!/usr/bin/env python

#list(mutable, append, insert, pop, sort, reverse, del, index, count, remove)
mylist = sequence(0,100)
#Tuples(immutable,union, diff, issubset, remove, pop, clear )
myset = {'value1', 4.5, True, 10}
#dictionaries(mutable, keys(), values(), items(), get(key(alt),)
mydict = {'first_key':1, 'second_key': True, 'third_key': [1,2,3,4]}

def add_seq():

    seq= range(0,100,3)
    print seq

add_seq()
