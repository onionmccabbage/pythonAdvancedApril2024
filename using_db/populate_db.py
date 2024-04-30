import sqlite3

def populateCreatures(creatures):
    '''iterate over the incoming creatures tuple
    populate the database with each creature from the tuple'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st = '''
    INSERT INTO zoo
    VALUES (?, ?, ?)
    '''
    for item in creatures:
        '''gate-keeping design pattern would be a good choice here'''
        try:
            # [on_true] if [expression] else [on_false] 
            n = item['creature'] if type(item['creature']==str) else 'Penguin'
            # or more voerbose:
            if type(item['creature']==str):
                n = item['creature']
            else:
                raise Exception('Creature name must be a string')
            if type(item['count']==int):
                count = item['count']
            else:
                raise Exception('Creeature count must be an integer')
            if isinstance(item['cost'], float):
                cost = item['cost']
            else:
                raise Exception('Creature cost must be a floating point number')
            # if all good we get here
            curs.execute(st, (n, count, cost))
            conn.commit()
        except Exception as err:
            print(err)
    conn.close() # only close when all done



if __name__ == '__main__':
    # here is a tuple of dict structures
    creatures_t = ( # normally this comes from JSON or API etc.
        {'creature':'Albatros', 'count':1,      'cost':120.99},
        {'creature':'Bear',     'count':5,      'cost':323.56},
        {'creature':'Carp',     'count':120,    'cost':87.00},
        {'creature':'Deer',     'count':121,    'cost':12.99},
        {'creature':'Elk',      'count':7,      'cost':73.47},
    ) 
    populateCreatures(creatures_t)