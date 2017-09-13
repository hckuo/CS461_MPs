#!/bin/bash

netid=hckuo2
python tweakedCertbuilder.py $netid template.cer
dd bs=1 count=256 skip=4 if=template.cer of=prefix.cer
IV=$(openssl dgst -md5 prefix.cer | awk '{print $2}')
echo $IV
./fastcoll -i $IV -o b1file b2file
python 1.2.5.py b1file b2file

