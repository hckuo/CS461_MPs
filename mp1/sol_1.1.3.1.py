import sys, hashlib

text1_file = sys.argv[1]
text2_file = sys.argv[2]
output_file = sys.argv[3]

# str1 and str2 have to be binary strings
def hammingDistance(str1, str2):
    assert len(str1) == len(str2)
    count = 0
    for i in xrange(len(str1)):
        if str1[i] == str2[i]:
            pass
        else:
            count += 1
    return count


with open(text1_file) as f:
    text1 = f.read().strip()
    f.close()

with open(text2_file) as f:
    text2 = f.read().strip()
    f.close()

h1 = hashlib.sha256(text1).hexdigest()
h2 = hashlib.sha256(text2).hexdigest()
binary_str1 = bin(int(h1, 16))[2:]
binary_str2 = bin(int(h2, 16))[2:]
print h1
print h2

d = hammingDistance(binary_str1, binary_str2)
print d, hex(d)

with open(output_file, 'w') as f:
    f.write(hex(d)[2:])
    f.close()
