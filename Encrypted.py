import re

def decode():
    fh = open('DizzyD.txt')
    bob = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']
    sandy = ['r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']
    for line in fh:
        for letter in bob:
            return(chr(ord(letter)+9))
        for letters in sandy:
            return(chr(ord(letters)-17))
        print('DizzyD.txt')

decode()
