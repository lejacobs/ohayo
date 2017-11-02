#! /bin/bash
mpc stop > /dev/null
mpc clear > /dev/null
mpc load http://provisioning.streamtheworld.com/pls/KDFCFM.pls > /dev/null
mpc play > /dev/null
mpc status > /dev/null
echo Content-type: text/html
echo

cat << EOF

<HTML>

<meta http-equiv="Refresh" content="1; url=/">

</HTML>
