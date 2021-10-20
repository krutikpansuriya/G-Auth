from os import system, name
from gauth import get_totp
import time
import sys


'''Replace XXX's with your token value'''
secret = b'XXXXXXXXXXXXXXX' 
a = get_totp(secret)
system('clear')
print ("--------------------")
sys.stdout.write('\rCode is : {:06d}'.format(a))
print ("\n\r--------------------")
while True:
	system('clear')
	print("--------------------")
	num = get_totp(secret)
        sys.stdout.write('\rCode is : {:06d}'.format(num))
        print ("\n\r--------------------")
        for i in range(30,0,-1):
                sys.stdout.write('\rThe code will change in : {:02d}'.format(i))
		sys.stdout.flush()
                time.sleep(1)

