from __future__ import division
from operator import mul
import numpy as np
from fractions import gcd


def read_from_file(filename):
    with open(filename, 'r') as f:
        content = f.read().strip()
        f.close()
    return content


def get_private_key(e, p, q):
    # follow the equation in Section 2.1 of the paper
    
    d = (1/e) % ( (p-1) * (q-1) )
    return d


if __name__=='__main__':
    
    mod_filename = 'moduli.hex'
    
    public_e = 65537
    
    moduli = read_from_file(mod_filename)
    moduli = moduli.splitlines()
    
    ########################################################
    # NOTE: Commnet this next line for Full list of 10100 moduli
    ########################################################
    moduli = moduli[0:100]  # for testing shorten the list
    
    # change into int
    moduli = [int(moduli[i], 16) for i in range(0, len(moduli))]
    
    #print moduli
    #print len(moduli)
    
    product = reduce(mul, moduli, 1)
    #print "Product is" , product
    
    # mining p and q
    # following the Algorithm in Section 3.3
    pi = []
    qi = []
    for i in range(0, len(moduli)):
        
        ni2 = np.power(moduli[i], 2)
        zi  = product % ni2
        p = gcd(moduli[i],zi/moduli[i])
        pi.append(p)
        qi.append(moduli[i] / p)
   
    
    print pi
    #print qi
    
    
    private_key = []
    for i in range(0, len(moduli)):
        d = get_private_key(public_e, pi[i], qi[i])
        print d
        private_key.append(d)
    
    print private_key
    # TODO: need to depcrypt the file using public key
    
    print "end"