# we may need to pip install flask (or similar)
from flask import Flask

# Flask is a proper web server, handling basic HTTP requests and serving HTML content
app = Flask(__name__) # any name will do, we often just use __name__
# Flask is all about handling HTTP routes
@app.route('/') # this is the root of our server
def root():
    '''Here we decide what content we will return to the user'''
    return 'Flask server is running'

# Often we consume Flask content in a browser, but equally we could use curl, postman, a custom client etc.
@app.route('/hello') # this will be a route to http://localhost:5000/hello
def hello():
    return 'Hello and welcome to flask routing (remember to re-start the server for changes)'

@app.route('/home')
def home():
    '''the home page'''
    # we might call some other microservce to rab data which we then return nicely formatted in HTML
    content = '<h2>We may write HTML</h2><p>This is the home page</p>'
    return content

if __name__ == '__main__':
    app.run() # this starts our Flask server