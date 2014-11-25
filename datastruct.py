from timeit import Timer

#listing ex.

def test1():
    #create a list by concat
    list1 = []
    for i in range(1000):
        list1 = list1 + [i]

def test2():
    #append
    list1 = []
    for i in range(1000):
        list1.append(i)

def test3():
    #list comprehension
    list1 = [i for i in range(1000)]
    

def test4():
    #list range
    list1 = list(range(1000))
    

#t1 = Timer("test1()", "from __main__ import test1")
#print("concat ",t1.timeit(number=1000), "milliseconds")
#t2 = Timer("test2()", "from __main__ import test2")
#print("append ",t2.timeit(number=1000), "milliseconds")
#t3 = Timer("test3()", "from __main__ import test3")
#print("comprehension ",t3.timeit(number=1000), "milliseconds")
#t4 = Timer("test4()", "from __main__ import test4")
#print("list range ",t4.timeit(number=1000), "milliseconds")


"""Efficiency of List Operators in Python

index [] O(1)
index assignment O(1)
append O(1)
pop() O(1)
pop(i) O(n)
insert(i,item) O(n)
del operator O(n)
iteration O(n)
contains (in) O(n)
get slice [x:y] O(k)
del slice O(n)
set slice O(n+k)
reverse O(n)
concatenate O(k)
sort O(n log n)
multiply O(nk)
"""
