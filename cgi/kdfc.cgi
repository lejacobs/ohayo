#! /bin/bash
mpc stop > /dev/null
mpc clear > /dev/null
mpc load http://provisioning.streamtheworld.com/pls/KDFCFM.pls > /dev/null
mpc play > /dev/null
mpc status > /dev/null
echo -e "Location: http://ohayo/index.html\n\n"
