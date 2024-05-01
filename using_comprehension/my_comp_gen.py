# remember generators can yield endless streams of values without persisting them in memory

# my_num_l = [n for n in range(-99, 100)] # persist in memory in a list
my_num_g = (n*n for n in range(-99, 100)) # start, stop-before, step
print(my_num_g)

# comprehnsively use each member of a clolleciton (comprehension)
a = (n for n in [1,2,3,4,5]) # list comprehension
b = (n for n in (1,2,3,4,5)) # tuple comprehension

odd_g = (n for n in range(3, 9) if n%2==1) # but more efficient just to say range(3, 9, 2)

# we can write our own custom generator
def myGen(first=0, last=10**10, step=1):
    '''generate values and yield results without persisting them in memory'''
    number = first
    while number < last: # while True makes an endless generator
        yield number**0.5 # when we put yield into a function, we make a generator
        number += step

if __name__ == '__main__':
    g = myGen() # we need an instance of our generator
    print(type(g)) # a generator
    print(g.__next__()) # 
    print(g.__next__()) #
    print(g.__next__()) # 
    print(g.__next__()) # 
    for _ in g:
        pass
        # print(_)
    
    # when we have exhausted the generator there will be no values left