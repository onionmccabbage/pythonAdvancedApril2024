# the zip library in Python has nothing to do with compression, archives or the like

def main():
    ''' we can use zip to combine collections '''
    days_l = ['Mon', 'Tues', 'Weds', 'Thurs']
    fruit_t = ('Banana', 'Orange', 'Kiwi', 'Durian')
    drinks_s = {'Coffee', 'Tea', 'Water', 'Calpico'}

    # zip will combine members from collection - only matching the name ordinal members
    z = zip(days_l, fruit_t, drinks_s)
    print(z, type(z)) # we have a zip object!
    for day, fruit, drink in z:
        print('On {0} we offer {1} with {2}'.format(day, fruit, drink))

if __name__ == '__main__':
    main()