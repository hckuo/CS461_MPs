import urllib2
import binascii as ba
import os
import copy

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

def change_to_hex(input_val):
    """input val should be a string"""
    return hex(int(input_val, 16)).rstrip("L").lstrip("0x")


if __name__=='__main__':

    netid = "mhasan11"

    hexdata = read_from_file("1.2.3_ciphertext.hex")
    # hexdata = change_to_hex(hexdata)  # change to a hex variable
    # print(hexdata)

    blocksize = 16  # we have 16 bytes block
    n_blocks = len(hexdata)/blocksize # total number of blocks

    # this is the list of all blocks
    block_list = list(hexdata[0+i:blocksize+i] for i in range(0, len(hexdata), blocksize))
    # change to hex values
    # block_list = [change_to_hex(blocks) for blocks in block_list]

    # print(n_blocks)
    # print(block_list)

    # iv = "".zfill(blocksize)  # the initialization vector, set to zero
    iv = "0".zfill(blocksize)  # the initialization vector, set to zero
    #iv = change_to_hex(iv)

    iv = copy.deepcopy(block_list[0])  # first iv is block 0
    #iv = change_to_hex(iv)
    print(iv)
    # print(hex(int(iv, 16)))


    # todo: need to XOR with padding value also

    val = hex(int(iv,16) ^ int(block_list[0], 16))
    print(val)



    # print(iv+block_list[0])
    msg = iv+block_list[0]  # TODO we need to update this iteratively
    #msg = change_to_hex(msg)
    #print(hex(int(msg, 16)))

    print(msg)

    msg_url = "http://192.17.90.133:9999/mp1/"+netid+"/?"+msg
    # msg_url = "http://127.0.0.1:8081/mp1/test/?"+msg  # for local server

    command = "curl " + msg_url
    # print(command)

    # TODO: need to check how to get_status() method work -- always gives 500 error to me
    get_status(msg_url)



    # os.system("curl http://192.17.90.133:9999/mp1/mhasan11/?$(cat 1.2.3_ciphertext.hex)")
    # os.system(command)  # this works (but showing padding error)
