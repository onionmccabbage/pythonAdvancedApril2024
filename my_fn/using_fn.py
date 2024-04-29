# these utilites could easily exist in another module
import functools # this gives us access to 'reduce'

def isOdd(n):
    '''return True if odd, False otherwise'''
    return n%2 !=0 # % means integer division (modulo)

def addThem(m, n):
    '''return the sum of m and n'''
    return m+n

def main():
    '''Here we exercise our code'''
    print(isOdd(3)) # True
    print(addThem(-42, 42)) # 0
    r = range(0,11)
    results = map(isOdd, r) # take evert value from 'r' and apply to our fn
    print(results) # we have a map object
    print(results.__next__()) # False (0)
    print(results.__next__()) # True  (1)
    print(results.__next__()) # False  (2)
    for _ in results: # True False, True...
        print(f' then we have {_}') # often use _ as the iterable
    # there are no values left on our map iterable
    # print(results.__next__()) # fail

    odds = filter(isOdd, (-7, -6, -5, -4, -3)) # odds is an iterable filter object containing all matching values
    print(odds)
    print(odds.__next__())

    # using reduce
    total = functools.reduce( addThem, range(0,16) ) # 0-15

    # we need a bunch of values
    t = tuple(r)
    total_odds = functools.reduce( addThem, t)
    print(total_odds)
    print(total)

if __name__ == '__main__':
    main()