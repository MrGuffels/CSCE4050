import sys
import time
from utils_demo import *

def main():
    file_number = [1,2,3]
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
        possible = 2**24
        start_time = time.time()
        print ('Total Possible Keys: '+str(possible))
        percent=possible/100
        counter = int(percent)+1
        for j in range(possible):
            if j == counter:
                current_time = time.time()
                print ('Percent Complete: '+str(int((counter/possible)*100)) + '% in ' + str(current_time-start_time) + ' seconds.')
                counter = counter + int(percent)
            #print (i)
            bytestring = bitstring_to_bytes(bin(2 ** 127 + j))
            new_message_bytes = decryptor_CTR(cipher_list,nonce_list,bytestring)
            if new_message_bytes == message_bytes:
                print('File '+ str(i) +'Solution Found:'+str(bin(j)))
                key=i
                break
    if key == -1:
            print ("No Solution Found")

main()