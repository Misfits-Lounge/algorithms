'''Sorting algorithms in python from
http://danishmujeeb.com/blog/2014/01/basic-sorting-algorithms-implemented-in-python
'''


import random


def return_random():
    return [random.randint(-50, 100) for i in xrange(32)]


#expect any LIST input
def bubble_sort(items):
    '''The name says it all, bubble sort
    http://en.wikipedia.org/wiki/Bubble_sort
    '''
    for i in xrange(len(items)):
        for j in xrange(len(items) - 1 - i):
            if items[j] > items[j+1]:
                print items[j]
                items[j], items[j+1] = items[j+1], items[j]
                
    print 'after sort', items

#bubble_sort(return)


def insertion_sort(items):
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j -1]:
            print i, j
            items[j], items[j - 1] = items[j - 1], items[j]
            j -= 1
    return items


print insertion_sort(return_random())
