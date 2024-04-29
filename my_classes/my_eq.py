# we can override ANY built-in feature of Python
# anything with dunder (leading and trailing double underscore) belongs to Python

class Word: # implicitly inherit from object
    '''Override the meaning of equality 
    In this example, we will declare equality to be case insensitive'''
    def __init__(self, text):
        self.text = text # NB here we are NOT using mangling or property get/set
    def __eq__(self, other):
        '''instead of normal equality, we will chck equality after forcing to lower case'''
        answer = self.text.lower() == other.text.lower()
        return answer
    
if __name__ == '__main__':
    word1 = Word('hello')
    word2 = Word('Hello')
    print( word1 == word2 ) # this wil invoke our overriden __eq__

# __ne__ not equal
# __gt__ greater than
# __lt__ less than
# __ge__ and __le__ greater-or-equal and less-or-equal

# other 'magic methods'
# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other
# __len__ is the length of the objec