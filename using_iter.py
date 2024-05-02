# we can make anything iterable
class Evens:
    '''this class lets us iterate over even numbers'''
    def __init__(self, limit):
        self.__limit = limit
        self.__start = 0
    def __iter__(self):
        '''to make a class iterable, simply override the __iter__ method'''
        return self # simple as that
    def __next__(self):
        '''once the class is iterable wealso overide __next__'''
        if self.__start > self.__limit:
            raise StopIteration # our iterable is exhausted
        else:
            rval = self.__start
            self.__start +=2
            return rval

def main():
    '''exercise the code'''
    e = Evens(10) # an instance of our iterable class
    print(e.__next__()) # 0
    print(e.__next__()) # 2
    print(e.__next__()) # 4
    for _ in e:
        print(f'next is {_}')

if __name__ == '__main__':
    main()