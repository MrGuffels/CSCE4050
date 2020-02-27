import sys
import time
from utils_demo import *

def main():
    #file_number = [1,2,3]
    file_number = [1]
    key=-1
    for i in file_number:
        print("File set "+str(i))
        #Read cipher#.bin into memory
        cipher_list = read_bytes('files/c'+str(i)+'.bin')
        #Read nonce#.bin into memory
        nonce_list = read_bytes('files/nonce'+str(i)+'.bin')
        #Read m#.txt into memory
        message_bytes = string_to_bytes(open('files/m'+str(i)+'.txt',"r").read())
        print (message_bytes)
        #Brute force exhaustive search sub function
        for i in range(2**24):
            print (i)
            bytestring = bitstring_to_bytes(bin(2 ** 127 + i))
            new_message_bytes = decryptor_CTR(cipher_list,nonce_list,bytestring)
            if new_message_bytes == message_bytes:
                print("Solution Found:"+str(i))
                key=i
                break
        if key == -1:
            print ("No Solution Found")

main()