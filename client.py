import socket
import time

# Indicates if the network was interrupted during send. 
# When it's False, everything is working as is should.
# If the network goes down when we are still sending we set this to True
flag = False    

packets_to_send = 10

multaddr = '224.0.0.100'
port = 12345
mgroup = (multaddr, port)

svcid = 1

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 0)

for k in range(1, packets_to_send+1):
    #msg = 'maddr:' + multaddr + ',port: ' + str(port) + ' pkg_No: ' + str(k)
    msg  = 'Request\t: ' + str(svcid) + '\n'
    msg += 'pkg_No\t: ' + str(k) 
    msg += "\n" + str(int(packets_to_send-k)) + " packets remaining"
    try:
        sock.sendto(msg.encode(), mgroup)
    except OSError as error:
        print("Client: Something went wrong with the connection.")
        flag = True
        break
    #time.sleep(0.001)

if not flag:
    print("Client: Sent " + str(k) + " packets")
else:
    print("Client: " + str(k-1) + " packets were sent instead of " + str(packets_to_send))
