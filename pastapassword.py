#!/usr/bin/env python3

import os
import string
import time

os.system("test -d ~/.pastapass || mkdir ~/.pastapass")
print("====================")
print("Welcome to PastaPass")
print("====================")
print()

def menu():
    print("(C) Create New Password")
    print("(D) Display Password")
    print("(H) Help")
    print("(L) List Accounts on Profile")
    print()

def display():
	display_request = input("Name of Service/Platform: ")
	os.system('cat ~/.pastapass/' + display_request)
	time.sleep(1)

def help():
	os.system('nano ~/pastapass/README')

def create():
	create_name = input("Name your password (e.g. facebook): ")
	create_password = input("Create a password: ")
	com1 = 'echo ' + create_password + ' >>' + ' ~/.pastapass/' + create_name
	os.system(com1)
	 

menu()
a = input()
if (a == 'd'):
	display()
elif (a == 'h'):
	help()
elif (a == 'c'):
	create()
else:
	print('Invalid Input')
