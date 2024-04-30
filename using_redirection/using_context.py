from contextlib import contextmanager
import sys

@contextmanager # this decorator lets us handle context easily
def outputRedirect( newOutput ):
    '''redirect any printed output to our new output stream'''
    old_stdout = sys.stdout # we will remember what the original stdout is
    sys.stdout = newOutput
    # NB if any finction uses 'yield' then it can keep running after the end
    yield # instead of 'return' we 'yield'
    #  when we are done...
    sys.stdout = old_stdout # put things back how they were

def main():
    '''exercise our code'''
    print('normal printed output is directed to the console')
    try:
        with open('my_stream.txt', 'a') as fobj:
            with outputRedirect(fobj):
                # at this point the context is now 'outputRedirect' using 'fobj'
                print('this goes to our text file')
                sys.stdout.write('more context-switched output')
                print('\n')
        # when 'with' is done, there is nothing left to yield, so the context is swiched back
        print('all back to normal')
    except Exception as err:
        print(err)

if __name__== '__main__':
    main()