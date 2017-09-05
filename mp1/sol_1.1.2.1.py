import sys
cipertext_file = sys.argv[1]
key_file = sys.argv[2]
output_file = sys.argv[3]
print cipertext_file, key_file, output_file
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
table = {}
with open(key_file) as f:
    key = f.read().strip()
    f.close()
    print key

for i in range(26):
    table[key[i]] = alphabet[i]

with open(cipertext_file) as f:
    cipertext = f.read().strip()
    print cipertext
    f.close()

plaintext = ''
for l in cipertext:
    if l in table:
        plaintext += table[l]
    else:
        plaintext += l
print plaintext

with open(output_file, 'w') as f:
    f.write(plaintext)
    f.close()
