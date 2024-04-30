def printTofile(t):
    '''write the text to a persistent file using print'''
    # we ought to try-except here
    fout = open('my_log.txt', 'a') # 'a' will append text
    print(t, file=fout) # this will default ot a new line character
    fout.close()

def writeToFile(t):
    '''use a file access object to progressivewly write to a file'''

def readText():
    '''retrieve text from a persistent file'''

def seekContent(n):
    '''seek content within a text file'''

if __name__ == '__main__':
    printTofile('that was easy')