import socket
from socket import *
import os
import sys
import struct
import time
import select
import binascii
from statistics import stdev

ICMP_ECHO_REQUEST = 8

packet_max = float('-inf')
packet_min = float('+inf')
packet_avg = 0
stdev_var = [0,0,0,0]
packet_cnt = 0

def checksum(string):
    csum = 0
    countTo = (len(string) // 2) * 2
    count = 0

    while count < countTo:
        thisVal = (string[count + 1]) * 256 + (string[count])
        csum += thisVal
        csum &= 0xffffffff
        count += 2

    if countTo < len(string):
        csum += (string[len(string) - 1])
        csum &= 0xffffffff

    csum = (csum >> 16) + (csum & 0xffff)
    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer


def receiveOnePing(mySocket, ID, timeout, destAddr):
    global delay, packet_cnt, packet_max, packet_min, packet_avg, stdev_var
    timeLeft = timeout
    while 1:
        startedSelect = time.time()
        whatReady = select.select([mySocket], [], [], timeLeft)
        howLongInSelect = (time.time() - startedSelect)
        if whatReady[0] == []:  # Timeout
            return "Request timed out."
        timeReceived = time.time()
        recPacket, addr = mySocket.recvfrom(1024)
        # Fill in start
        # Fetch the ICMP header from the IP packet

        icmpHeader = recPacket[20:28]
        type, code, checksum, id, seq = struct.unpack('bbHHh', recPacket[20:28])
        bytesInDouble = struct.calcsize('d')
        timeData = struct.unpack('d', recPacket[28:28 + bytesInDouble])[0]
        delay = round((timeReceived - timeData) * 1000)
        packet_min = min(packet_min, delay)
        packet_max = max(packet_max, delay)
        stdev_var[packet_cnt] = delay ;
        packet_cnt += 1
        packet_avg = (packet_min + packet_max) / 2

        ip_header = struct.unpack('!BBHHHBBH4s4s', recPacket[:20])

        return delay

        #return timeReceived - timeData

        timeLeft = timeLeft - howLongInSelect
        if timeLeft <= 0:
            return "Request timed out."


def sendOnePing(mySocket, destAddr, ID):
    # Header is type (8), code (8), checksum (16), id (16), sequence (16)
    myChecksum = 0
    # Make a dummy header with a 0 checksum
    # struct -- Interpret strings as packed binary data

    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    data = struct.pack("d", time.time())
    # Calculate the checksum on the data and the dummy header.
    myChecksum = checksum(header + data)
    # Get the right checksum, and put in the header
    # Convert 16-bit integers from host to network byte order
    if sys.platform == 'darwin':
        myChecksum = htons(myChecksum) & 0xffff
    else:
        myChecksum = htons(myChecksum)
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    packet = header + data
    mySocket.sendto(packet, (destAddr, 1)) # AF_INET address must be tuple, not str

     # Both LISTS and TUPLES consist of a number of objects
     # which can be referenced by their position number within the object.


def doOnePing(destAddr, timeout):
    icmp = getprotobyname("icmp")

    # SOCK_RAW is a powerful socket type. For more details: http://sockraw.org/papers/sock_raw

    mySocket = socket(AF_INET, SOCK_RAW, icmp)
    myID = os.getpid() & 0xFFFF
    sendOnePing(mySocket, destAddr, myID)
    delay = receiveOnePing(mySocket, myID, timeout, destAddr)
    mySocket.close()
    return delay


def ping(host, timeout=1):
    global delay, packet_max, packet_min, packet_avg, stdev_var
    #timeout=1 means: If one second goes by without a reply from the server, # the client assumes that either the client's ping or the server's pong is lost
    dest = gethostbyname(host)
    vars = []
    print("Pinging " + dest + " using Python:")
    print("")
    # Calculate vars values and return them
    # Send ping requests to a server separated by approximately one second
    for i in range(0,4):
        delay = doOnePing(dest, timeout)
        #print(delay)
        time.sleep(1) #change me to 1

    #vars = [float(round(packet_min , 2)), float(round(packet_avg , 2)), float(round(packet_max , 2)), float(round((stdev(stdev_var)), 2))] # change me to 2
    vars.append(str(round(packet_min , 2)))
    vars.append(str(round(packet_avg , 2)))
    vars.append(str(round(packet_max , 2)))
    vars.append(str(round((stdev(stdev_var)) ,2)))
    return vars

if __name__ == '__main__':
   ping("google.co.il")
