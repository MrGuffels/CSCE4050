import sys

def main():
    file_number = [1,2,3]
    for i in file_number:
        print("File set "+str(i))
        cipher_list = read_bin('files/c'+str(i)+'.bin')
        #Read nonce#.bin into memory
        #Read m#.txt into memory

        #Brute force exhaustive search sub function

        #Return the key in hex and print it
        print ("Cipher Text: ", end="")
        print (cipher_list)

def read_bin(filename):
    byte_decimal_list = []
    with open(filename, "rb") as binary_file:
        byte = binary_file.read(1)
        while byte:

            # print(byte) #Print byte as its' ascii equivallent 
            # print (ord(byte)) #Convert byte to decimal and print
            # print(bin(int.from_bytes(byte, byteorder=sys.byteorder))) #Converts byte to binary bits and print

            byte_decimal_list.append(ord(byte))
            
            byte = binary_file.read(1)
    return byte_decimal_list

main()