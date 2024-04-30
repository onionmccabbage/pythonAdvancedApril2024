def printTofile(t):
    '''write the text to a persistent file using print'''
    # we ought to try-except here
    fout = open('my_log.txt', 'a') # 'a' will append text
    print(t, file=fout) # this will default ot a new line character
    fout.close()

def writeToFile(t):
    '''use a file access object to progressively write to a file'''
    try:
        # using 'b' will read/write bytes
        fout = open('my_log.txt', 'at') # 'x' for exclusive access, 'w' will (over)write
        size = len(t)
        offset = 0
        chunk = 12
        while True:
            if offset > size:
                fout.write('\n') # we may choose to end with a new line character
                break
            else:
                part = t[offset: offset+chunk]  # here we use slicing
                part_b = part.encode() # if we need to write bytes
                # or part_b = b'this will be bytes'
                fout.write(part)
                offset += chunk
        fout.close()
    except Exception as err:
        print(err)

def readText():
    '''retrieve text from a persistent file'''
    fin = open('my_log.txt', 'rt')
    # r = fin.read() # read back the whole thing
    # r = fin.readline() # read back a line
    r = fin.readlines() # read back all lines into a list
    fin.close()
    return r

def seekContent(n=18):
    '''seek content within a text file'''
    try:
        fin = open('my_log.txt', 'r')
        fin.seek(n) # move the file cursor to position n
        the_Rest = fin.read()
        fin.close()
        return the_Rest
    except Exception as err:
        print(err)

if __name__ == '__main__':
    printTofile('that was easy')
    nonsense = '''Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?'''
    writeToFile(nonsense)
    retrieved = readText()
    print(retrieved)
    print( seekContent(20) )