#second backend code
'''
connect
accept message
send message
'''
import socket
def server_connection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET-> ipv4 address family,SOCK_STREAM- > TCP socket
    sock.bind((socket.gethostname(),1034)) #assigns ip address and port number
    sock.listen(5) #5 connections can be queued for this socket by operating system
    m = input("Enter morse code : ")

    while True:
        clt, adr = sock.accept() #used to accept a connection
        print(f"Connection to {adr} established")
        clt.send(bytes(m, "utf-8"))
        break
    return

def close():
    clt.close()

    
        
