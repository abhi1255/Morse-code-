import mct.client
import mct.server

x = 1
while x>0:
    print("Enter 1 to recieve the message : ")
    print("Enter 2 to translate the message : ")
    print("Enter 0 to exit :")
    x = int(input("Enter your choice : "))

    if x == 1:
        mct.server.client_connect()

    elif x == 2:
        tr = mct.server.translate()
        print("Message is :",tr)

