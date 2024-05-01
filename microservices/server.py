import socket # this provides all we need to make microservices

def server():
    '''This microservice will listen for http calls and respond'''
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # localhost is 127.0.0.1
    port_t = ('localhost', 9874) # choose suitable values
    server.bind(port_t) # bind to our microservice address
    server.listen() # we need our server to liten for clients
    print(f'Server is running on {port_t[0]} {port_t[1]}')
    # we need a run loop
    while True:
        (client, addr) = server.accept() # host addr and port
        buf = client.recv(1024) # we often choose how much to receive
        print(f'Server has received {buf} from {client}')
        break # always provide a means of ending the loop


if __name__ == '__main__':
    server() # invoke our microservice