#!/usr/bin/env python



class BaseClass(object):
    def __init__(self, name="class"):
        self.name = name
        
    def get_name(self):
        return self.name

    def __str__(self):
        return "class"


print BaseClass()
