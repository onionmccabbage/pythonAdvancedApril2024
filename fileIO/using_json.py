# json is currently the most popular data-transfer format
import json  # this is aprt of python

def makeJson(s):
    '''convert the data structure 's' into a json text'''
    j = json.dumps(s) # dump the python structure to json text
    return j

def retrieve(j):
    '''convert json into a Python data structure'''
    try:
        s = json.loads(j) # convert the (valid) json text into a python structure
        return s
    except Exception as err:
        print(err)
# Valid JSON:
# ALL text members are in double quotes
# All numeric and boolean are literal
# every open element must also close
# one container for everything


if __name__ == '__main__':
    # here is a tuple of  dictionaries
    creatures_t = ( # normally this comes from JSON or API etc.
        {'creature':'Albatros', 'count':1,      'cost':120.99},
        {'creature':'Bear',     'count':5,      'cost':323.56},
        {'creature':'Carp',     'count':120,    'cost':87.00},
        {'creature':'Deer',     'count':121,    'cost':12.99},
        {'creature':'Elk',      'count':7,      'cost':73.47},
    )
    # nb the tuple is immutable, but the members of the tuple are not
    # creatures_t[3]['count'] = 211
    # print(creatures_t)
    creatures_j = makeJson(creatures_t)
    print(creatures_j, type(creatures_j))
    creatures = retrieve(creatures_j)
    print(creatures, type(creatures))