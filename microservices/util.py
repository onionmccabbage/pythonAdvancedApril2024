# make some bytes
def makeBytes(v):
    b = bytes(v)
    return b

if __name__ == '__main__':
    values = range(0,256)
    b = makeBytes(values)
    print(b)