


class debugger(object):
    def __init__(self, function):
        self.function = function
    '''and this is where the function gets passed
    '''
    def __call__(self):
        print function.__name__
        print function.__doc__


@debugger
def get_x():
    '''this is the document
    '''
    print "I got here"
    


get_x()
