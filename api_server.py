import socket
import struct
import sys 
import platform
from time import sleep as sleep

#todo: if on internet, the router forwards*2 the packets!!! Need to fix this.
#todo: user to select interface or address to listen on !!!!
#todo: remove the api_server import and functionality somehow.


# the multicast address to join
multaddr = '224.0.0.100'
port = 12345
mgroup = (multaddr, port)

# available services
# Keys
# 1: Server available for connection
# 2: Server available to calculate prime
# Values
# 0: Means the server is not registered for this service.
# 1: Means the server is     registered for this service
SVCIDS = {1:0, 2:0}
#SVCIDS = {1: "ConnectionAvailable", 2: "CalculatePrime"}

# open UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Enables the socket to be reusable 
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# TTL should be set to 1 in order for our packets to not get forwarded 
# outside the local network by some router. Even if by default a router
# would drop it, we set this option here explicitly.
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)

# Passing '' as an address means all interfaces. The joining happens 
# by setting the socket option:  socket.IP_ADD_MEMBERSHIP (see register)
# Same as sock.bind(('0.0.0.0', port))
sock.bind(('', port))

# ONLY for linux, get the available IP addresses through `hostname` command.
if platform.system()=="Linux":
    print("________________________")
    from subprocess import check_output
    ips = check_output(['hostname', '--all-ip-addresses'])
    print("usable ip addresses on this system: " + str(ips[0:len(str(ips))-6]))
    print("________________________")
else:
    ips = b''


#  Become a member of the multicast group
member_req = socket.inet_aton(multaddr) + socket.inet_aton('0.0.0.0')
print("________________________________________________")
try:
    sock.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP, member_req)
except OSError as error :
    if platform.system() =="Linux":
        if len(str(ips)) == 5:
            print("There is no connection on this device.")
    else:
        print(format(error))
    quit()


# Get our ip
ip = socket.gethostbyname(socket.gethostname())




def register(svcid):
    if not (svcid in SVCIDS.keys()):
        print("Unknown service id \t: " + str(svcid))
        print(SVCIDS)
        return
    if SVCIDS[svcid] == 0 :
        SVCIDS[svcid] = 1
    else:
        print("Already registered for this service")
    

# If a server-host has already joined a group with IP_ADD_MEMBERSHIP, the option
# IP_DROP_MEMBERSHIP will not stop the server from receiving packets destined for 
# that group.
def unregister(svcid):
    if not (svcid in SVCIDS.keys()):
        print("Unknown service id \t: " + str(svcid))
        print(SVCIDS)
        return
    if SVCIDS[svcid] == 1:
        SVCIDS[svcid] = 0
    else:
        print("Unregistration not needed. (You was not registered)")
    #member_req = struct.pack('=4sl', socket.inet_aton(multaddr), socket.INADDR_ANY)
    #member_req = socket.inet_aton(multaddr) + socket.inet_aton('0.0.0.0')
    #if not (svcid in SVCIDS.keys()):
    #    print('\t==== Tried to unregister from an unsupported service, id \t: ' + str(svcid))
    #    print(SVCIDS)
    #try:
    #    sock.setsockopt(socket.SOL_IP, socket.IP_DROP_MEMBERSHIP, member_req)
    #except OSError as error:
    #    if (error.errno == 99):
    #        print("\t==== You tried to un-register an already unregistered server.")
    #        print("\t==== Your action was not successful.")
    #        return
    #    elif (error.errno == 19):
    #        print("\t==== There was a problem with your connection during un-registration.")
    #        return
    #    else:
    #        print(format(error))
            
    #print("Server unregistered of service: " + str(svcid))
    #print("________________________________________________")

def getRequest(svcid, buffer, length):
    data, address = sock.recvfrom(1024)
    print("Sender info: " + str(address))
    print("========================  MSG START")
    print(data.decode())
    print("========================  MSG END")
    
    #print(sock.recv(length))
    
    #data, sender = sock.recvfrom(1024)
    #while data[-1:] ==  '\0':   # remove trailing \0
    #    data = data[:-1]
    #print("from :" + str(sender) + " " + repr(data))

def sendReply(reqid, buffer, length):
    pass
