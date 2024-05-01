import doctest

def cubeIt(a, b):
    '''return all the bubes of integers between a and b
    Doctest lets us write unit tests within the doc string
    >>> cubeIt(3, 6)
    [27, 64, 125]
    >>> cubeIt(0, 101) # doctest:+ELLIPSIS
    [0, 1, 8, ..., 1000000]
    '''
    answers = []
    for i in range(a, b):
        answers.append(i**3)
    return answers

if __name__ == '__main__':
    # print( cubeIt(3, 6) )
    doctest.testmod(verbose=True)