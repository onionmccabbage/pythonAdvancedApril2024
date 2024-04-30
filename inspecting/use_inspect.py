import inspect
 
def type_validator(func):
    pars = inspect.signature(func)
    def newFunc(*args, **kwargs):
        arguments = pars.bind(*args, **kwargs).arguments
        for arg, value in arguments.items():
            if not isinstance(value, func.__annotations__[arg]):
                raise TypeError('Incorrect type for ' + arg)
        return func(*args, **kwargs)
    return newFunc
 
@type_validator # always the immediately following function is passedf in to the decorator
def add(a: int, b: int):
    return a + b
 
add(2,3) # returns 5
add('c', 4) # returns type-error
# has context menu