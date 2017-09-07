import urllib2
def get_status(u):
    req = urllib2.Request(u)
    try:
        f = urllib2.urlopen(req)
        print f.code
    except urllib2.HTTPError, e:
        print e.code


def read_from_file(filename):

    with open(filename, 'r') as f:
        content = f.read()

    return content


if __name__=='__main__':

    hexdata = read_from_file("1.2.3_ciphertext.hex")
    hexdata = hex(hexdata)
    #print(hexdata)

    blocksize = 16
    print("number of blocks", hexdata/blocksize)
