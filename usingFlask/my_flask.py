# we may need to pip install flask (or similar)
from flask import Flask, render_template
import requests # we need this for proxying

# Flask is a proper web server, handling basic HTTP requests and serving HTML content
app = Flask(__name__) # any name will do, we often just use __name__
# Flask is all about handling HTTP routes
@app.route('/') # this is the root of our server
def root():
    '''Here we decide what content we will return to the user'''
    return 'Flask server is running'

# Often we consume Flask content in a browser, but equally we could use curl, postman, a custom client etc.
@app.route('/hello') # this will be a route to http://localhost:5000/hello
@app.route('/hi')
@app.route('/ciao')
def hello():
    return 'Hello and welcome to flask routing (remember to re-start the server for changes)'

@app.route('/home')
def home():
    '''the home page'''
    # we might call some other microservce to rab data which we then return nicely formatted in HTML
    content = '<h2>We may write HTML</h2><p>This is the home page</p>'
    return content

# routes with parameters: REST Represent State Transfer
# Note - more than one route can end up sending the same content
@app.route('/greet')
@app.route('/greet/<name>') # here we allow one argument, called 'name'
def greet(name='Timnit'): # provide sensible default values
    '''return a page containing a variable'''
    content = f'<h2>Greetings {name}</h2>'
    return content

# we can make our server a proxy
# e.g. grab from https://jsonplaceholder.typicode.com
@app.route('/json') # be careful - you may need to check CORS permissions
@app.route('/json/<cat>')
@app.route('/json/<cat>/<id>')
def j(cat='albums', id=1):
    response = requests.get(f'https://jsonplaceholder.typicode.com/{cat}/{id}')
    response_j = response.json() # or xml, text, html etc.
    return response_j

@app.route('/web')
def web():
    return render_template('lunch.html')





if __name__ == '__main__':
    app.run() # this starts our Flask server