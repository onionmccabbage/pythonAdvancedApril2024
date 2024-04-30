import sqlite3

def customUpdate(w): # w will be an instance of a creeature (to be updated)
    '''update the DB based on creature 'w' '''
    q = int(float(w['count'])) # a bit of validation
    a = w['creature']
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # in SQL strings are in quotes, other values are NOT
    st = f'''
    UPDATE zoo
    SET count={q}
    WHERE creature = "{a}"
    '''
    # print(st)
    curs.execute(st)
    conn.commit() # without this, the executed SQL does NOT alter the DB
    conn.close()


if __name__ == '__main__':
    # declare an updated creature
    p = {'creature':'Penguin', 'count':9, 'cost':432.99}
    customUpdate(p)