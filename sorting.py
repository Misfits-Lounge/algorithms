#!/usr/bin/env python

import random

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

if __name__ == '__main__':
    sentence = raw_input("Enter a short sentence, no special chars: ")
    best_match()
