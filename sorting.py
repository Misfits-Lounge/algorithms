#!/usr/bin/env python

import random
matching = {}
matched = False


def generate_string():
    alp = 'abcdefghijklmnopqrstuvwxyz '
    genstr = ''
    for i in range(len(sentence)):
        genstr = genstr + alp[random.randrange(len(alp))]
    return genstr

def index_string(generated_string):
    matched = 0
    for i in range(len(generated_string)):
        if sentence[i] == generated_string[i]:
            matched +=1
    return matched / float(len(sentence))


def best_match():
    best = 0
    newstring = generate_string()
    new = index_string(newstring)
    mil = 0
    count = 0
    while best < 1:
        if new > best:
            best = new
            print 'The best so far', best, '% of goal sentence >>>', newstring
            print 'Goal sentence is " ', sentence, ' "'
        newstring = generate_string()
        new = index_string(newstring)
        count +=1
        if (count % 1000000) == 0:
            mil +=1
            print 'We got to', mil, 'Milion'

#a bit more complex implementation would be to generate a random char from a-z and match to every char in the word
"""done, but there's a bug that doesn't update the dict sometimes """

def gen_char():
    """get me a random char from a-z including a space """
    char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !@#$%^&*()_+|}{":?><-=][\;\'\/.,"'
    return_char =  char_list[random.randrange(len(char_list))]
    return return_char

    
def index_char(randchar, matching, looped):
    """check first if we have an array match already and extract
    the position of the char in the given sentence 
    """
    [matching.setdefault(i, randchar) for i in range(len(sentence)) if sentence[i] == randchar]
    if randchar in matching.values():
        looped +=1
    return looped

    
def iterable():
    """generate a char"""
    looped, returned, tries = 0, 0, 0
    while returned < len(sentence):
        if returned != 0:
            returned = index_char(gen_char(), matching, returned)
        else:
            returned = index_char(gen_char(), matching, looped)
        tries += 1
    print "It took %s tries to guess the phrase entered" % tries
    print sentence
    print matching

if __name__ == '__main__':
    sentence = raw_input("Enter a short sentence: ")
    best_match()
    iterable() 
