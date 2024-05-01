import socket

def client():
    '''this client will make requests to our microservice over http'''
    # match whatever our server is expecting
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_t = ('localhost', 9874) 
    sock.connect( port_t ) # we now connect to our server
    #send a message to our server
    message = 'hello' # or b'hello'
    sock.send(message.encode()) # make sure we encode as bytes

if __name__ == '__main__':
    client()