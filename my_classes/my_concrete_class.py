#when we import, Python will run the imported code exactly as if it was written here
from my_abstract_class import AbstractShape

class Shape(AbstractShape):
    __slots__ = ('__s_name','__sides') # a tuple of permitted properties
    def __init__(self, s_name, sides):
        '''call the internal validation setter method'''
        self.s_name = s_name # this will call the setter method
        self.sides = sides
    @property
    def s_name(self): # getter method
        return self.__s_name # this is called name mangling
    @s_name.setter    # setter method
    def s_name(self, new_name):
        '''validate the property'''
        if type(new_name)==str and new_name != '': # not permitting empty string
            self.__s_name = new_name
        else:
            raise TypeError('Name must be a non-empty string') # or we can just set a sensible default
    @property
    def sides(self):
        return self.__sides
    @sides.setter
    def sides(self, num_sides):
        if type(num_sides)==int or num_sides<1 : # or in (int, float)
            self.__sides = num_sides
        else:
            self.__sides = 4 # set a sensible default
    def __str__(self):
        '''we override the built-in __str__ to specify how this class should print'''
        return f'This is the Shape class called {self.s_name} with {self.sides} sides\n' # \n we may choose to include new line
    
# it is really good practice to use the following...
# (avoid running code when imported elsewhere)
if __name__ == '__main__':
    try:
        s = Shape('Oblong', 4) # we have an instance of our class (calls __init__)
        s.s_name = 'Square'  #this will call the internal validated setter method
        # can we access the name-mangled property?
        # s.__s_name = 'wibblywoo' # this fails due to slots
        s2 = Shape('Circle', 1) 
        s3 = Shape('Triangle', 3)
        print(s, s2, s3, sep='')
        print(s2)
        print(s3, end=', ')
        # we can still acces the mangled property name
        print( s._Shape__s_name )
    except TypeError as te:
        print(f'Problem: {te}')
    except Exception as err:
        print(err)
    finally: # this block will ALWAYS run
        pass

