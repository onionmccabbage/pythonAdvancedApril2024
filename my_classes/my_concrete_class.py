
class Shape:
    def __init__(self, s_name):
        if type(s_name) == str:
            self.s_name = s_name
        else:
            self.s_name = 'unknown'
    def __str__(self):
        '''we override the built-in __str__ to specify how this class should print'''
        return f'This is the Shape class called {self.s_name}\n' # we may choose to include new line
    
if __name__ == '__main__':
    s = Shape(True) # we have an instance of our class (calls __init__)
    s.s_name = -99
    s2 = Shape('Circle') 
    s3 = Shape('Triangle')
    print(s, s2, s3)

