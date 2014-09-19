#!/usr/bin/env python3
import random

goal = 'black car'

def generatestr(strlen):
    alp = "abcdefghijklmnopqrstuvwxyz "
    result = ""
    for i in range(strlen):
        result = result + alp[random.randrange(27)]
    return result

def indexstr(goal, genstr):
    matched = 0
    for i in range(len(goal)):
        if goal[i] == genstr[i]:
            matched +=1 
    return matched / len(goal)

def iterateover():
    newstring = generatestr(len(goal))
    bestguess = 0
    newguess = indexstr(goal, newstring)
    looped = 0
    while bestguess < 1:
        if 0 == (looped % 1000000) :
            print ('This is the best guess', bestguess)
        if newguess > bestguess:
            print(newguess, newstring)
            bestguess = newguess
        newstring = generatestr(len(goal))
        newguess = indexstr(goal, newstring)
        looped +=1
iterateover()
