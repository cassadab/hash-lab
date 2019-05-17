# Farmhash function
import constants
import ctypes



def mur(input):
    print(constants.hi)

def fmix(input):
    input32 = ctypes.c_uint32(input)
    input32.value ^= input >> 16
    input32.value *= 0x85ebca6b;
    input ^= input >> 13;
    input32.value *= 0xc2b2ae35;
    input32.value ^= input >> 16;
    hash = hex(input32.value)
    hash = hash[2:]
    hash = hash[:-1]
    print(hash)

num_in = 0 
while(num_in != -1):
    print("Enter a number to hash")
    num = int(input())
    fmix(num)
