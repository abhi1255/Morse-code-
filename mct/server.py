#first backend code
'''
connect
recieve message
translate from morse to normal characters
display the message
'''

import socket

'''
def morse_input():
    m_input = input("Enter required morse code message : ")
    return m_input
'''


def client_connect():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((socket.gethostname(), 1034))
    #print(sock.stillconnected()) 

def translate():    
    morse_trnsl = ''

    while True:
        morse_code = sock.recv(7)
        if len(morse_code) <= 0:
            break
        morse_trnsl += morse_code.decode("utf-8")
    print(morse_trnsl)
    
    mdict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H','..': 'I', '.---': 'J', '-.-': 'K',
             '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
             '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
             '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'}
    x = ''
    y = morse_trnsl.split()
    flag = False
    for i in y:
        if i in mdict:
            x += " "
            x += str(mdict[i])
            flag = True
        else:
            flag = False
            break
    if flag == True:
        #print("Transalted message is : ",x)
        return x
    else:
        return ("Invalid morse code")
    sock.close()
    

'''
def translate(tobetr):
    mdict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H','..': 'I', '.---': 'J', '-.-': 'K',
             '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
             '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
             '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'}
    x = ''
    y = tobetr.split()
    
    for i in y:
        if i in mdict:
            x += str(mdict[i])
    return x
'''
