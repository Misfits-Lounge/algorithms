#!/usr/bin/env python



class BaseClass(object):
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
