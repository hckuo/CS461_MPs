#!/bin/bash

netid=hckuo2
python tweakedCertbuilder.py $netid template.cer # generate tempate certificate
dd bs=1 count=192 skip=4 if=template.cer of=prefix.cer # truncate "the to-be-signed" part where the modulus bytes start as prefix
IV=$(openssl dgst -md5 prefix.cer | awk '{print $2}') # compute md5(prefix) as inital vector to produce collisions with fastcoll
echo $IV
./fastcoll -i $IV -o b1file b2file
python 1.2.5.py b1file b2file # use these two collisions files as inputs as b1, b2 described in the paper

