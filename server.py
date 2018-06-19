import socket
import sys
from flightlib import *

def main():
    """
    The main module
    """
    try:
        #create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
        sys.exit();
    
    print 'Socket created'

    server_address = ('localhost', 10000)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    sock.bind(server_address)


    # Listen for connections
    sock.listen(1)

    while True:
        # Wait for a connection
        connection, client_address = sock.accept()

        try:
            print >>sys.stderr, 'connection from', client_address

            # Receive the data and answer to it
            while True:
                fc = FlightControllerConversation()
                data = connection.recv(16)
                if data:
                    # import pdb;pdb.set_trace()
                    # Step 1: Decode data
                    message = fc.decode_request(data)
                    # Step 2: Generate answer
                    answer = fc.order_response(message)
                    connection.send(answer)
                
        finally:
            # Close the connection connection
            connection.close()

if __name__ == '__main__':
    main()