# import socket module
from socket import *
import sys  # In order to terminate the program


def webServer(port=13331):
    serverName = '127.0.0.1'

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
            message = "click here now"
            filename = message.split()[1]
            f = open("helloworld.html")
            outputdata = f

            # Send one HTTP header line into socket
            # Fill in start

            # Fill in end

            for i in range(0, len(outputdata)):
                connectionSocket.send('HTTP/1.0 200 OK\nContent-Type: text/html\n\n')
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()

        except IOError:
            connectionSocket.send('HTTP/1.0 404 file not found\nContent-Type: text/html\n\n')
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()

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
