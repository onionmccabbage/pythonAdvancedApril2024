# historically we used urllib for API access
import requests # may need to pip install requests

APIUrl = 'https://jsonplaceholder.typicode.com/'

def getAllUsers():
    '''retrieve all users from the API end-point'''
    # be careful - we often try to avoid polluting the global name-space
    global APIUrl # we now have access to the global APIUrl asset
    usersUrl = f'{APIUrl}users'
    r = util(usersUrl)
    return r

def getOneUser(n=3):
    '''retrieve one user id=n'''
    global APIUrl # we now have access to the global APIUrl asset
    oneUserUrl = f'{APIUrl}users/{n}'
    r = util(oneUserUrl)
    return r

def util(u):
    response_obj = requests.get(u)
    res_j = response_obj.json() # or .text .html .xml
    return res_j

if __name__ == '__main__':
    users = getAllUsers()
    print(users)
    one = getOneUser()
    print(one)