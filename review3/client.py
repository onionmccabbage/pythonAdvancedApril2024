# we can build a socket client
import socket
import sys

def client():
    '''this is a basic socket client to interact with our socket server'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_t = ('localhost', 9874)
    # connect to the server
    client.connect(port_t)
    # send a message to the server
    # check to see if additional arguments were passed in
    if len(sys.argv) > 1:
        # check if we have a valid catgory
        valid_cat_t = ('users', 'posts', 'todos', 'photos', 'albums')
        c = sys.argv[1]
        if c in valid_cat_t:
            message = '/'.join(sys.argv[1:])
        else:
            message = ' '.join(sys.argv[1:]) # ignore the module name!
    else:
        message = 'default message'
    client.send( message.encode() )
    # if anything comes back from the server, handle it here
    data = client.recv(1024)
    print(f'Client received {data}')
    client.close()

if __name__ == '__main__':
    client()