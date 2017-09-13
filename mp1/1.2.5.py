from Crypto.Util import number
from fractions import gcd
import sys

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
	lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
	x, lastx = lastx - quotient*x, x
	y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m


def iscoprime(a, b):
    return gcd(a, b) == 1

def isdivisible(a, b):
    return b % a == 0

def add_trailing_bits(a, num_bits):
    return (a << num_bits) | ((2 << num_bits) -1)

e = 65537
def output_factors(p1, p2, q1, q2):
    outfileA = 'sol_1.2.5_factorsA.hex'
    outfileB = 'sol_1.2.5_factorsB.hex'
    with open(outfileA, 'w') as f:
        f.write(hex(p1)[2:]+'\n')
        f.write(hex(q1)[2:]+'\n')
        f.close()
    with open(outfileB, 'w') as f:
        f.write(hex(p2)[2:]+'\n')
        f.write(hex(q2)[2:]+'\n')
        f.close()

def output_cert(p1, p2, q1, q2):
    import tweakedCertbuilder as cb
    from cryptography.hazmat.primitives.serialization import Encoding
    outfileA = 'sol_1.2.5_certA.cer'
    outfileB = 'sol_1.2.5_certB.cer'
    netid = 'hckuo2'
    privkey1, pubkey1 = cb.make_privkey(p1, q1)
    certA = cb.make_cert(netid, pubkey1)

    privkey2, pubkey2 = cb.make_privkey(p2, q2)
    certB = cb.make_cert(netid, pubkey2)

    print certA.signature.encode('hex')
    print certB.signature.encode('hex')

    with open(outfileA, 'wb') as f:
        f.write(certA.public_bytes(Encoding.DER))
        f.close()

    with open(outfileB, 'wb') as f:
        f.write(certB.public_bytes(Encoding.DER))
        f.close()

if __name__=='__main__':
    b1file = sys.argv[1]
    b2file = sys.argv[2]
    with open(b1file) as f:
        b1 = f.read()
        f.close()

    with open(b2file) as f:
        b2 = f.read()
        f.close()

    b1 = int(b1.encode('hex'), 16)
    b2 = int(b2.encode('hex'), 16)

    while True:
        p1 = number.getPrime(512)
        p2 = number.getPrime(512)
        if iscoprime(p1-1, e) and iscoprime(p2-1, e):
            print 'p1 =', p1
            print 'p2 =', p2
        else:
            continue
        b1t, b2t = add_trailing_bits(b1, 1024), add_trailing_bits(b2, 1024)
        p1p2 = p1 * p2
        M1, M2 = p2, p1
        t1, t2 = modinv(M1, p1), modinv(M2, p2)
        b0 =  (p1 - (b1t % p1)) * M1 * t1 + (p2 - (b2t % p2)) * M2 * t2 # chinese reminder theorem
        b0 = b0 % p1p2
        if isdivisible(p1, b1t + b0) and isdivisible(p2, b2t + b0):
            print 'b0 = ', b0
        else:
            raise ValueError
        k = 0
        while True:
            if k % 1000 == 0:
                print k
            b = b0 + k * p1p2
            n1, n2 = b1t + b, b2t + b
            q1, q2 = n1/p1, n2/p2
            if number.isPrime(q1) and number.isPrime(q2) and iscoprime(e, q1-1) and iscoprime(e, q2-1):
                break
            else:
                if k > (2 << 1024):
                    break
                k = k + 1
                continue
        print 'k = ', k
        output_factors(p1, p2, q1, q2)
        output_cert(p1, p2, q1, q2)
        break

