# create a new database (or use an existing one)
# also, create a table within the database

import sqlite3 # Python comes with an instance of SQL Lite DB

def accessDB():
    '''Create or use a database for zoo creatures
    Each creature will have a count and a cost'''
    # Python uses a Database Access Object - it never directly interacts with the DB
    conn = sqlite3.connect('my_db') # at this point, the DB is created or accessed
    curs = conn.cursor() # this lets us work with the database
    # to achieve anything we need an SQL statement
    # tripple-quotes let us use white-space such as neew line characters
    st = ''' 
    CREATE TABLE zoo
    (
        creature VARCHAR(32) PRIMARY KEY,
        count int,
        cost float
    )
    '''
    try:
        conn.execute(st) # we use the cursor to send thet SQL statement to the database
        conn.commit() # if al worked out fine, we commit the changes
        conn.close() # tidy up  -release resources no longer needed
    except Exception as err:
        print(err)

if __name__ == '__main__':
    accessDB()


# some other DB conn mechanisms
# see https://wiki.python.org/moin/DatabaseInterfaces
# DB2
# import DB2 # remember to pip install first!!
# conn = DB2.connect(dsn='ibm-DB', uid='analyst', pwd='db2pwd')

# Sybase
# import Sybase
# conn = Sybase.connect('SYBASE', 'username', 'passwd', 'databasename')

# Oracle
# import cx_Oracle
# conn = cx_Oracle.connect('username', 'passwd', 'hostname:port/SID')
# conn2 = cx_Oracle.connect('username/passwd@hostname:portno/SID')
# dsn_tns = cx_Oracle.makedsn('hostname', portno, 'SID')
# conn3 = cx_Oracle.connect('username', 'passwd', dsn_tns)

# MySQL
# import MySQLdb
# conn = MySQLdb.connect(host = "hostname", user = "username", passwd = "password", db = "dbname")

# PySQLite
# from pysqlite2 import dbapi2 as sqlite
# conn = sqlite.connect("mydb", connectionproperties)

# ODBC
# import odbc
# conn = odbc. odbc("myDSN/username/password")