# create a new database (or use an existing one)
# also, create a table within the database

import sqlite3 # Python comes with an instance of SQL Lite DB

def accessDB():
    '''Create or use a database for zoo creatures
    Each creature will have a count and a cost'''
    conn = sqlite3.connect('my_db') # at this point, the DB is created or accessed
    curs = conn.cursor() # this lets us work with the database
    # to achieve anything we need an SQL statement
    # tripple-quotes let us use white-space such as neew line characters
    st = ''' 
    CREATE TABLE zoo
    {
        creature VARCHAR(32) PRIMARY KEY,
        count int,
        cost float
    }
    '''
    try:
        conn.execute(st) # we use the cursor to send thet SQL statement to the database
        conn.commit() # if al worked out fine, we commit the changes
        conn.close() # tidy up  -release resources no longer needed
    except Exception as err:
        print(err)

if __name__ == '__main__':
    accessDB()