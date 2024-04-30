# redirection is when we override the default input or output stream
# there is a stdin and an stdout
import sys

# remember: print uses __str__ but immediate mode python uses __repr__

class RedirectOutput():
    '''Redirect output to a different stream then recover the original output stream'''
    def __init__(self, new_stdout):
        self.stdout = new_stdout # called ONCE on first instantiation
    def __enter__(self):
        '''__enter__ is invoked whenever the class instance is used'''
        self.orig_stdout = sys.stdout
        sys.stdout = self.stdout
    def __exit__(self, exc_type, exc_value, exc_traceback): # we MUST pass all these
        '''__exit__ is invoked whenever the instance finishes operation'''
        sys.stdout = self.orig_stdout # put things back how they were

def main():
    '''exercise our code'''
    try:
        with open('my_log.txt', 'a') as fout:
            r = RedirectOutput(fout) # we pass our file access object as an output stream
            try:
                with r: # this calles __enter__ then __exit__
                    print('this will be redirected to our file output stream')
            except Exception as err:
                print(err)
    except Exception as err:
        print(err)
    finally:
        print('all back to the original output stream')

if __name__ == '__main__':
    print(sys.stdout)
    sys.stdout.write('oooh thats clever')
    main()