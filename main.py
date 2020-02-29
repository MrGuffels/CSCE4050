import sys
import time
from utils_demo import *

#Key is 0b110000001100101010111010
#Takes 5 minutes on average to find.

def main():
    key=-1                                                  #Holding place for the key
    message_bytes,cipher_list,nonce_list = getFileParts(1)  #Read information from files
    #Brute force exhaustive search sub function
    possible = 2**24
    start_time = time.time()        #Time for progress meter
    print ('Total Possible Keys: '+str(possible))   
    percent=possible/100
    counter = int(percent)+1
    for j in range(possible):       #For loop from 0 to possible-1
        if j == counter:            #Used for progress meter
            current_time = time.time()
            print ('Percent Complete: '+str(int((counter/possible)*100)) + '% in ' + str(current_time-start_time) + ' seconds.')
            counter = counter + int(percent)
        bytestring = bitstring_to_bytes(bin(2 ** 127 + j))  #Create bytestring adding j
        new_message_bytes = decryptor_CTR(cipher_list,nonce_list,bytestring)    #Run information through decryption
        if new_message_bytes == message_bytes:              #If new_message is same as message
            print('File 1 Solution Found:'+str(bytestring))
            key=j
            break
    if key == -1:
            print ("No Solution Found")
    else:                                                   #This checks to verify that 2 and 3 also work with the found key
        bytestring = bitstring_to_bytes(bin(2 ** 127 + key))
        message_bytes,cipher_list,nonce_list = getFileParts(2)
        new_message_bytes = decryptor_CTR(cipher_list,nonce_list,bytestring)
        if new_message_bytes == message_bytes:
            print('File 2 Solution Found:'+str(bytestring))
        else:
            print("That key doesn't work with File 2")
        message_bytes,cipher_list,nonce_list = getFileParts(3)
        new_message_bytes = decryptor_CTR(cipher_list,nonce_list,bytestring)
        if new_message_bytes == message_bytes:
            print('File 3 Solution Found:'+str(bytestring))
        else:
            print("That key doesn't work with File 3")

def getFileParts(i):
    print("File set "+str(i))
    #Read cipher#.bin into memory
    cipher_list = read_bytes('files/c'+str(i)+'.bin')
    #Read nonce#.bin into memory
    nonce_list = read_bytes('files/nonce'+str(i)+'.bin')
    #Read m#.txt into memory
    message_bytes = string_to_bytes(open('files/m'+str(i)+'.txt',"r").read())
    return message_bytes,cipher_list,nonce_list

main()