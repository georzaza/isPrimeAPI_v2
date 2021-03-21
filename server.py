from time import sleep as sleep
import pathlib

# include of the api_server module
try:
    from api_is_prime import api_server as server
except (ModuleNotFoundError):
    import sys
    path=str(pathlib.Path().absolute())
    sys.path.append(path)
    print("Module api_is_prime is not installed globally on your system.\nTo install it, read the install_api_globally.txt file.\nAs a workaround " + path + " was added to your Python Path.")
    try:
        from api_is_prime import api_server as server
    except (ModuleNotFoundError):
        print('\nNope. This will not work.\nYou have 2 options:\n1. run this script while inside the folder that it resides\n2. install the api as a global module.\n\t File "install_api_globally" has instructions to do so.\nWe are now removing the' + path + ' from your Python Path\n\n')
        sys.path.remove(str(pathlib.Path().absolute()))
        quit()


#server.register(1)
flag = True

#server.getRequest(1, 0, 1024)
#print("first pkg received")
#server.getRequest(1, 0, 1024)
#print("second packet received.")
#server.unregister(1)
#server.getRequest(1, 0, 1024)
#print("got one packet when being unregistered.")

server.register(1)
k=0
while True:
    flag = not flag
    if flag:
        pass
    else:
        #server.register(1)
        pass
        #server.register(2)
    print("")
    print("Server: Listening ")
    server.getRequest(1, 100, 1024)
    k+=1
    print("Server: got "+str(k)+" packets.")
    #print("Server: Got one packet. Sleeping for 1 seconds now..")
    #sleep(1)
    #print("Server: sleep ended")
    #print("Server: going to unregister now -- Hint: unregistering is only done for testing")
    if flag:
        pass
        #server.unregister(1)
    else:
        pass
        #server.unregister(2)    
