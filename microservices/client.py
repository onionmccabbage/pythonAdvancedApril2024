import socket
import sys
import util

def client(b=b''):
    '''this client will make requests to our microservice over http'''
    # match whatever our server is expecting
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_t = ('localhost', 9874) 
    sock.connect( port_t ) # we now connect to our server
    #send a message to our server
    if len(sys.argv) > 1: # ignore sys.argv[0]
        message = ' '.join(sys.argv[1:]) # slicing
    else:
        message = 'hello from the client' # or b'hello'

    sock.send(message.encode() + b) # make sure we encode as bytes
    # if any response is returned, receive it here
    data = sock.recv(1024) # read up to 1024 bytes
    print(f'Client received {data}')
    sock.close()


if __name__ == '__main__':
    b = util.makeBytes(range(0,64))
    client(b)