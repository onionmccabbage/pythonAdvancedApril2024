class MyClass():
    def __init__(self) -> None: # type hints
        pass
    def __str__(self) -> str: # the type hint is a nice documentation for others looking at this code
        pass

class Duck():
    '''we may declare properties and methods that belong to the class (rather than to instances)'''
    count = 0 # this property belongs to the duck class
    def __init__(self, name):
        self.name = name
        Duck.count += 1 # we also have -= *= but not ++ or --

    def __str__(self):
        return f'This duck is called {self.name}'
    @classmethod # the following method belongs to the class (rather than to an instance of the class)
    def howMany(cls):
        return f'There are {cls.count} ducks'
    
if __name__ == '__main__':
    d1 = Duck('Howard')
    d2 = Duck('Ethel')
    d3 = Duck('Downy')
    print(d1, d2, d3)
    # how many ducks
    print(Duck.count)
    print(Duck.howMany())