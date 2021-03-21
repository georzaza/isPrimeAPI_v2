import socket

mgroup = '224.0.0.100'
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

def sendRequest(svcid, buffer, length):
    pass

def getReply(reqid, buffer, length, block):
    pass