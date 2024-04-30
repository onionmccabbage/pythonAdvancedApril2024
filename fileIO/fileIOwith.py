# 'with' will make use of an asset and close the asset when no longer required

def writeWith(t):
    ''' use the with operator '''
    with open('my_log.txt', 'a') as fout:
        fout.write(t)
    # no need to close, when the 'with' completes it will tidy up

if __name__ == '__main__':
    writeWith('now that was easy')