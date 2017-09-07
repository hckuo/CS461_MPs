import urllib2
import binascii as ba


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

    netid = "mhasan11"

    hexdata = read_from_file("1.2.3_ciphertext.hex")
    # hexdata = ba.unhexlify(hexdata)
    print(hexdata)

    blocksize = 16  # we have 16 bytes block
    n_blocks = len(hexdata)/blocksize # total number of blocks

    # this is the list of all blocks
    block_list = list(hexdata[0+i:blocksize+i] for i in range(0, len(hexdata), blocksize))

    # print(n_blocks)
    # print(block_list)

    iv = "".zfill(blocksize)  # the initialization vector, set to zero

    # print(iv+block_list[0])
    msg = iv+block_list[0]  # TODO we need to update this iteratively
    # msg_url = "http://192.17.90.133:9999/mp1/${"+netid+"}/?"+msg
    msg_url = "http://192.17.90.133:9999/mp1/"+netid+"/?"+hexdata
    print(msg_url)
    # get_status(msg_url)
    get_status(msg_url)
