# we will write a custom decorator
# the purpose is to show any and every argument passed in to ANY function

def showArgs(f): # remember - we can pass ANYTHING in to a function
    '''reveal all the positional and keyword arguments of any function'''
    def newfunc(*args, **kwargs):
        print(f'Running a function called {f.__name__}')
        print(f'\tThe positional arguments are {args}')
        print(f'\tThe keyword arguments are {kwargs}')
        return f(*args, **kwargs) # we return a call to the original function
    return newfunc

@showArgs # we apply our showArgs function as a custom decorator
def raisePower(m,n): # our decorator MUST take the immediately following function as its argument
    '''raise m to the power of n'''
    return m**n

if __name__ == '__main__':
    r = raisePower(3,4)
    print(r)