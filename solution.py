 #import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):

   serverName = 'RobsServer'

   serverPort = 13331

   serverSocket = socket(AF_INET, SOCK_STREAM)

   serverSocket.bind((serverName, serverPort))

   serverSocket.listen(1)  #Prepare a server socket

   #Fill in start

   #Fill in end

   while True:
       #Establish the connection
       #print('Server socket is ready to receive:')
       connectionSocket, addr = serverSocket.accept()
       connectionSocket.recv(13331).decode()

       #Fill in start      #Fill in end
       try:
           message = serverSocket.recv(13331)
           filename = message.split()[1]
           f = open(filename[1:])
           outputdata = f

           #Send one HTTP header line into socket
           #Fill in start

           #Fill in end

           #Send the content of the requested file to the client
           for i in range(0, len(outputdata)):
               connectionSocket.send(outputdata[i].encode())

           connectionSocket.send("\r\n".encode())
           #print('OK (200)')
     
       except IOError:
           #print('file not found (404)')
           #Send response message for file not found (404)
           #Fill in start

           #Fill in end

           #Close client socket
           #Fill in start

           #Fill in end
   connectionSocket.close()
   serverSocket.close()
   sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
   webServer(13331)
