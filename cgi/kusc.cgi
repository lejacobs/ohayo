#! /bin/bash
mpc stop
mpc clear
mpc load http://playerservices.streamtheworld.com/pls/KUSCMP128.pls
mpc play
mpc status
echo Content-type: text/html
echo

cat << EOF

<HTML>

<meta http-equiv="Refresh" content="1; url=/">

</HTML>
