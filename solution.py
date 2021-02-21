# import socket module
from socket import *
import sys  # In order to terminate the program
#test

def webServer(port=13331):

    serverPort = 13331

    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.bind(('', serverPort))

    serverSocket.listen(1)  # Prepare a server socket

    # Fill in start

    # Fill in end

    while True:
        # print('Ready to Serve...')
        connectionSocket, addr = serverSocket.accept()  # Establish the connection

        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]
            f = open(filename[1:], 'r')
            outputdata = f.read()

            x = open("helloworld.html", 'r')
            sendIt = x.read()

            statusUp = "HTTP/1.0 200 OK\r\n\r\n"
            connectionSocket.sendall(statusUp.encode())
            connectionSocket.sendall("\r\n\r\n".encode())
            # Send one HTTP header line into socket
            # Fill in start

            # Fill in end
            for i in range(0, len(outputdata)):
                connectionSocket.sendall("\r\n\r\n".encode())
            connectionSocket.close()

        except IOError:
            statusDown = "HTTP/1.0 404 file not found\r\n\r\n"   # Send response message for file not found (404)
            connectionSocket.sendall(statusDown.encode())
            connectionSocket.close()
            pass

        serverSocket.close()
        sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
