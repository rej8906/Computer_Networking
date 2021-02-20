# import socket module
from socket import *
import sys  # In order to terminate the program


def webServer(port=13331):
    serverName = 'RobsServer'

    serverPort = 13331

    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.bind((serverName, serverPort))

    serverSocket.listen(1)  # Prepare a server socket

    # Fill in start

    # Fill in end

    while True:
        # Establish the connection
        # print('Ready to Serve...')
        connectionSocket, addr = serverSocket.accept()
        connectionSocket.recv(13331).decode()

        # Fill in start      #Fill in end
        try:
            message = serverSocket.recv(13331)
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f

            # Send one HTTP header line into socket
            # Fill in start

            # Fill in end

            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n')
            connectionSocket.send("\r\n".encode())
            # print('OK (200)')

        except IOError:
            connectionSocket.send('HTTP/1.1 404 file not found\nContent-Type: text/html\n\n')
            # Send response message for file not found (404)
    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data
    # Fill in start

    # Fill in end

    # Close client socket
    # Fill in start

    # Fill in end

if __name__ == "__main__":
    webServer(13331)