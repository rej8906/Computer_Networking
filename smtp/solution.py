from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
   msg = "\r\n My message"
   endmsg = "\r\n.\r\n"

   mailserver = ('127.0.0.1', 1025) # Choose a mail server (e.g. Google mail server)

   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect((mailserver)) # Create socket called clientSocket and establish a TCP connection with mailserver and port

   recv = clientSocket.recv(1024).decode()
   #print(recv)
   #if recv[:3] != '220':
      #print('220 reply not received from server.')

   # Send HELO command and print server response.
   heloCommand = 'HELO Alice\r\n'
   clientSocket.send(heloCommand.encode())
   recv1 = clientSocket.recv(1024)
   recv1 = recv1.decode()
   #print(recv1)
   #if recv1[:3] != '250':
          #print('250 reply not received from server.')

   # Send MAIL FROM command and print server response.
   mailFrom = 'MAIL FROM: <xxxx>\r\n'
   clientSocket.send(mailFrom.encode())
   recv2 = clientSocket.recv(1024)
   recv2 = recv2.decode()
   #print("MAIL FROM:" + recv2)

   # Send RCPT TO command and print server response.

   rcptTo = 'RCPT TO: <xxxxx>\r\n'
   clientSocket.send(rcptTo.encode())
   recv3 = clientSocket.recv(1024)
   recv3 = recv3.decode()
   print("RCPT TO:" + recv3)

   # Send DATA command and print server response.
   data = 'data\r\n'
   clientSocket.send(data.encode())
   recv4 = clientSocket.recv(1024)
   recv4 = recv4.decode()
   print("Data:" + recv4)

   #Send message data.
   clientSocket.send(msg.encode())
   recv5 = clientSocket.recv(1024)
   recv5 = recv5.decode()
   print("Msg:" + recv5)

   # Message ends with a single period.
   clientSocket.send(endmsg.encode())
   recv6 = clientSocket.recv(1024)
   recv6 = recv6.decode()
   print("End:" + recv6)

   # Send QUIT command and get server response.
   quit = 'QUIT\r\n'
   clientSocket.send(quit.encode())
   recv7 = clientSocket.recv(1024)
   recv7 = recv7.decode()
   #print("End:" + recv7)
   clientSocket.close()

if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')