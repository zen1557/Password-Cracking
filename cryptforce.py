#!/usr/bin/python

import crypt
from termcolor import colored

def crackPass(cryptWord):
    salt = cryptWord[0:2]
    dictionary = open("dictionary.txt",'r') #you can add your txt file
    for word in dictionary.readlines():
        word = word.strip('\n')
        cryptPass = crypt.crypt(word, salt)
        if (cryptWord == cryptPass):
            print(colored("[+] Found Password: " + word, 'green'))
            return

def main():
    passFile = open('pass.txt','r') #You can add your pass.txt file
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptWord = line.split(':')[1].strip(' ').strip('\n')
            print(colored("[*] Cracking Password For: " + user, 'red'))
            crackPass(cryptWord)

main()            