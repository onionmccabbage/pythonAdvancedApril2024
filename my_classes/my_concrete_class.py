
class Shape:
    __slots__ = ('__s_name',) # a tuple of permitted properties
    def __init__(self, s_name):
        '''call the internal validation setter method'''
        self.s_name = s_name # this will call the setter method
    @property
    def s_name(self): # getter method
        return self.__s_name # this is called name mangling
    @s_name.setter    # setter method
    def s_name(self, new_name):
        '''validate the property'''
        if type(new_name)==str:
            self.__s_name = new_name
        else:
            raise TypeError # or we can just set a sensible default
    def __str__(self):
        '''we override the built-in __str__ to specify how this class should print'''
        return f'This is the Shape class called {self.s_name}\n' # we may choose to include new line
    
if __name__ == '__main__':
    s = Shape('Oblong') # we have an instance of our class (calls __init__)
    s.s_name = 'Square'  #this will call the internal validated setter method
    # can we access the name-mangled property?
    # s.__s_name = 'wibblywoo' # this fails due to slots
    s2 = Shape('Circle') 
    s3 = Shape('Triangle')
    print(s, s2, s3)
    # we can still acces the mangled property name
    print( s._Shape__s_name )

