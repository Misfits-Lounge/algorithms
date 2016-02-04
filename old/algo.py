
'''Unpacking variables
'''

#discarding values when unpacking, can use _ var for it

s = 'Hello'
data = ['ACME', 50, 91.1, (2012,12,21)]
_, shares, price, _ = data
#print shares, price

def anagram_check(string1, string2):
    '''compare the two strings
    see if chars match. conside that the first,
    is an anagram for the second. simplistic.
    
    As n gets large, the n2 term will dominate
    the n term and the 12 can be ignored. 
    Therefore, this solution is O(n2).
    '''
    #strings immutable, lists not that much
    list1 = list(string2)
    pos1 = 0
    cont = True
    while pos1 < len(string1) and cont:
        pos2 = 0
        found = False
        while pos2 < len(list1) and not found:
            if string1[pos1] == list1[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            list1[pos2] = None    #<--- None? why not just pop
        else:
            cont = False
        pos1 = pos1 + 1
    return cont

#print anagram_check('abcd', 'dcba')

def anagram_check2(string1, string2):
    '''At first glance you may be tempted to think
    that this algorithm is O(n), since there is one 
    simple iteration to compare the n characters 
    after the sorting process. However, the two calls
    to the Python sort method are not without their 
    own cost. As we will see in a later chapter, 
    sorting is typically either O(n2) or O(nlogn), 
    so the sorting operations dominate the iteration. 
    In the end, this algorithm will have the same order 
    of magnitude as that of the sorting process.
    '''
    list1 = sorted(list(string1))
    list2 = sorted(list(string2))
    pos = 0 
    matches = True
    while pos < len(string1) and matches:
        if list1[pos] == list2[pos]:
            pos = pos + 1
        else:
            matches = False
            
    return matches

#print anagram_check2('abcde', 'edcba')
    


def complex_range(string1, string2):
    #26 chars in the english alphabet
    char1 = [0] * 26
    char2 = [0] * 26
    for i in range(len(string1)):
        '''see what the position of the 
        char belongs to.
        the array is zero indexed based,
        so letter a is at pos 0,
        ord('a') is 97 ord('b') 98
        substracting ord('a') from any given 
        unicode char returns the alphabet 
        position of the char
        '''
        pos = ord(string1[i]) - ord('a')
        char1[pos] = char1[pos] + 1

    for i in range(len(string2)):
        pos = ord(string1[i]) - ord('a')
        char2[pos] = char2[pos] + 1

    j = 0
    cont = True
    while j < 26 and cont:
        if char1[j] == char2[j]:
            j =j + 1
        else:
            cont = False

    return cont

'''Again, the solution has a number of iterations.
 However, unlike the first solution, none of them are nested. 
The first two iterations used to count the characters are both 
based on n. The third iteration, comparing the two lists of counts, 
always takes 26 steps since there are 26 possible characters in 
the strings. Adding it all up gives us T(n)=2n+26 steps. 
That is O(n). We have found a linear order of magnitude algorithm
for solving this problem.

Before leaving this example, we need to say something about space
requirements. Although the last solution was able to run in linear
time, it could only do so by using additional storage to keep the
two lists of character counts. In other words, this algorithm 
sacrificed space in order to gain time.

This is a common occurrence. On many occasions you will need to
 make decisions between time and space trade-offs. In this case, 
the amount of extra space is not significant. However, if the
 underlying alphabet had millions of characters, there would be 
more concern. As a computer scientist, when given a choice of 
algorithms, it will be up to you to determine the best use of 
computing resources given a particular problem.
'''
#print complex_range('apple', 'pleap')
