'''
hard coded dictionary
run a loop iterating thru the dict
use get function
get each element and add to string
print the string
'''
import socket

morse = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.',
               'S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..',
                '9':'----.','0':'-----'}

keys = list(morse.keys())
values =  list(morse.values())

new_morse = {}
for i in range(0,len(keys)):
    new_morse[values[i]] = str(keys[i])
print(new_morse)
x = input("Enter your morse code")
morse_list = x.split()
print(morse_list)
 




















'''
usin = input("Enter your message")
split_list = usin.split()
values = morse.values()
print(values)
for i in split_list :
    if i in values:
        print(
'''        
