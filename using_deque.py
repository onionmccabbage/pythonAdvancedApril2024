from collections import deque

def checkPal(word):
    '''check to see if the word is a palindrome (reads the same forward or back)'''
    dq = deque(word)
    # print(type(dq))
    while len(dq)>1:
        left = dq.popleft()
        right = dq.pop()
        if left != right:
            return False
    return True

if __name__ == '__main__':
    result = checkPal('madam')
    print(result)
    result = checkPal('tenet')
    print(result)
    result = checkPal('racecar')
    print(result)
    result = checkPal('oops')
    print(result)