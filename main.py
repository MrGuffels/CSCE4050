import sys
import time
from utils_demo import *

key_leader = '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

def main():
    file_number = [1,2,3]
    for i in file_number:
        print("File set "+str(i))
        #Read cipher#.bin into memory
        cipher_list = read_bytes('files/c'+str(i)+'.bin')
        #Read nonce#.bin into memory
        nonce_list = read_bytes('files/nonce'+str(i)+'.bin')
        #Read m#.txt into memory
        message_bytes = string_to_bytes(open('files/m'+str(i)+'.txt',"r").read())
        #Brute force exhaustive search sub function
        for i in range(2**8):
            bytestring = bitstring_to_bytes(key_leader+format(i,'024b'))
            #print(key_leader+format(i,'024b'))
            print (bytestring)

        #Return the key in hex and print it
        print ("Cipher Text: ", end="")
        print (cipher_list)
        print ("Nonce Text: ",end="")
        print (nonce_list)
        print ("Message Text: ",end="")
        print (message_bytes)

main()