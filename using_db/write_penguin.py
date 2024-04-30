import sqlite3

def writePenguins():
    '''populate our DB with penguins'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st = '''
    INSERT INTO zoo
    VALUES ("Penguin", 16, 0.52)
    '''
    try:
        curs.execute(st)
        conn.commit()
        conn.close()
    except Exception as err:
        print(err)

if __name__ == '__main__':
    writePenguins()