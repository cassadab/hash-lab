# Farmhash function
import constants
import ctypes
import time
import string
import random
from constants import k2, k0

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
    c_int = ctypes.c_uint64()
    ctypes.memmove(ctypes.addressof(c_int), string, ctypes.sizeof(c_int))
    return c_int

# converts string to u_int32
def string_to_int32(string):
    c_int = ctypes.c_uint32()
    ctypes.memmove(ctypes.addressof(c_int), string, ctypes.sizeof(c_int))
    return c_int

# hashes a string of max length 16
def hash_string16(message, length):
    # print(message)
    c_k0 = ctypes.c_uint64(k0)
    c_k2 = ctypes.c_uint64(k2)
    c_string = ctypes.c_char_p(message)
    if(length >= 8):
        multiplier = ctypes.c_uint64(c_k2.value + length * 2)
        a = ctypes.c_uint64(string_to_int64(c_string).value + c_k2.value)
        b = ctypes.c_uint64(string_to_int64(c_string).value + length - 8)
        c = ctypes.c_uint64((b.value << 37) * multiplier.value + a.value)
        d = ctypes.c_uint64(((a.value >> 25) + b.value) * multiplier.value)
        return hash_len16(c, d, multiplier)
    if(length >= 4):
        multiplier = ctypes.c_uint64(c_k2.value + length * 2)
        a = string_to_int64(message)
        b = ctypes.c_uint64(string_to_int64(c_string).value + length - 4)
        a.value = 3 + a.value << 3
        return hash_len16(a, b, multiplier)
    if(len > 0):
        a = string_to_int32(message[0])
        b = string_to_int32(message[length >> 1])
        c = string_to_int32(message[length - 1])
        y = ctypes.c_uint32(a.value + (b.value << 8))
        z = ctypes.c_uint32(length + (c.value << 2))
        total = (y.value * c_k2.value ^ z.value * c_k0.value) * c_k2.value
        total_shifted = total ^ (total >> 47)
        return ctypes.c_uint64(total_shifted)
    return c_k2        

# helper method that shifts bits of max length 16 string
def hash_len16(u, v, mult):
    a = ctypes.c_uint64((u.value ^ v.value) * mult.value)
    a.value ^= (a.value >> 47)
    b = ctypes.c_uint64((v.value ^ a.value) * mult.value)
    b.value ^= (b.value >> 47)
    b.value *= mult.value
    return b

def random_string(string_length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))

# while(num_in != -1):
#     print("Enter a number to hash")
#     num = int(input())
#     fmix(num)

def time_trial(string_length):
    strings = generate_random_array(string_length)
    init_time = time.time()
    for s in strings:
        # print(s)
        hash_string16(s, len(s))
    end_time = time.time()
    total_time = end_time - init_time
    print(str(string_length) + '\t' + str(total_time) )
    

def generate_random_array(string_length):
    i = 0
    rand_array = [None] * 1000
    while i < 1000:
        rand_string = random_string(string_length)
        rand_array[i] = rand_string
        i += 1
    return rand_array

def time_tests():
    print('Size\tTime (s)')
    i = 1
    while i <= 16:
        time_trial(i)
        i += 1
    print('End of Time Trials')

time_tests()
# print(random_string(5)[0])