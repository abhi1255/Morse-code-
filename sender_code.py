import mct.client
import mct.server

x = 1
while x>0:
    print("Enter 1 to connect to other pc : ")
    print("Enter 2 to close connection :")
    print("Enter -1 to exit : ")
    x = int(input("Enter your choice : "))

    if x == 1:
        mct.client.server_connection()
'''
    elif x == 2:
        m = input("Enter morse code : ")
        mct.client.send(m)
'''       
    
