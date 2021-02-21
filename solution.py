# import socket module
from socket import *
import sys  # In order to terminate the program


def webServer(port=13331):

    serverPort = 13331

    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.bind(('', serverPort))

    serverSocket.listen(1)  # Prepare a server socket

    # Fill in start

    # Fill in end

    while True:
        # Establish the connection
        # print('Ready to Serve...')
        connectionSocket, addr = serverSocket.accept()

        # Fill in start      #Fill in end
        try:
            message = serverSocket.recvfrom(2048).decode()
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()

            statusUp = "HTTP/1.0 200 file not found\r\n"
            connectionSocket.send(statusUp.encode())
            connectionSocket.send("\r\n".encode())
            # Send one HTTP header line into socket
            # Fill in start

            # Fill in end
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
                connectionSocket.send("\r\n".encode())
                connectionSocket.close()

        except IOError:
            statusDown = "HTTP/1.0 404 file not found\r\n"
            connectionSocket.send(statusDown.encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
            pass

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
