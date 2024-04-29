from abc import ABCMeta, abstractmethod

class AbstractShape(metaclass=ABCMeta):
    '''This is an Abstract Base Class from which other concrete classes can take their lead'''
    def __init__(self):
        pass
    @abstractmethod
    def s_name(self):
        '''we never write ANY implementation in the absract'''
    @abstractmethod
    def __str__(self):
        '''we will definitiely need to implement a __str__ in our concrete classes'''

