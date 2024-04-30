import sqlite3

def customReadDB(w):
    '''read specific members back from our DB'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # we can select specific members using SELECT * FROM ... WHERE
    # we may use = or IS for exact matching
    # we may use WHERE creature LIKE "" to find partial matching
    # LIKE "%{w}" will match ends with w
    # LIKE "{w}%" will match begins with w
    # LIKE "%{w}%" will match contains w
    st = f'''SELECT creature, count, cost 
    FROM zoo 
    WHERE creature LIKE "%{w}%"  '''
    try:
        curs.execute(st)
        conn.commit()
        # we can now access stuff on the cursor
        rows = curs.fetchall() # grab every result from the executed SQL statement
        return rows
    except Exception as err:
        print(err)


if __name__ == '__main__':
    # we need to ask the user for which creature (should validate)
    w = input('Which creature? ') # NB EVERY user input is ALWAYS a string
    zoo = customReadDB(w)
    for animal in zoo:
        print(f'We have {animal[1]} {animal[0]} each costing {animal[2]}')