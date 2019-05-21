# Farmhash function
import constants
import ctypes

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
    print("\nHash: " + hash + "\n")

# Converts string to u_int64 
def string_to_int64(string):
    c_string = ctypes.c_char_p(string)
    c_int = ctypes.c_uint64()
    ctypes.memmove(ctypes.addressof(c_int), c_string, ctypes.sizeof(c_int))
    return c_int


# def hash_len0to64(message, length):


# num_in = 0 
# while(num_in != -1):
#     print("Enter a number to hash")
#     num = int(input())
#     fmix(num)

print(string_to_int64("wassup"))