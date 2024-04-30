import sqlite3

def readDB():
    '''read everything back from our DB'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # we can select everything using SELECT * FROM
    # Often we prefer to pick the members (and the order of the members)
    # st = '''SELECT * FROM zoo'''
    st = '''SELECT creature, count, cost FROM zoo'''
    try:
        curs.execute(st)
        conn.commit()
        # we can now access stuff on the cursor
        rows = curs.fetchall() # grab every result from the executed SQL statement
        return rows
    except Exception as err:
        print(err)


if __name__ == '__main__':
    zoo = readDB()
    for animal in zoo:
        print(f'We have {animal[1]} {animal[0]} each costing {animal[2]}')