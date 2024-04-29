# we will explore *args and **kwargs

def usePositional(*args): # here we choose to unpack the positional arguments
    '''this function expects only positional arguments'''
    print(args) # all the positional arguments now exist in a tuple called 'args'

def useKeywords(**kwargs): # we choose to gather the keyword arguments
    'this function expects only keyword arguments'
    print(kwargs) # all the keyword arguments always exist in a dictionary

def useBoth(*args, **kwargs): # keyword arguments must always follow any positional argument
    '''this function can accept positional and keyword arguments'''
    print(args) # all the positional arguments now exist in a tuple called 'args'
    print(kwargs) # all the keyword arguments always exist in a dictionary
    # we may choose to act conditionally based on how many args or the names of kwargs
    for k,v in kwargs:
        print(f'keyword argument {k} received a value {v}')

if __name__ == '__main__':
    # these arguments are at position 0, 1, 2, 3
    a = ('lunchtime', True, [], {'n':'Timnit'})
    b = {'x':-3, 'z':99}
    usePositional( 'hello', 543.21, True, [5,4,3] ) # a few positional arguments
    useKeywords(x=3, y=4, name='triangle', right=True)
    useBoth(*a, **b) # spread out the tuple and the dictionary