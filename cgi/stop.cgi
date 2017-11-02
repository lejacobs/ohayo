#! /bin/bash
mpc stop
mpc clear
echo Content-type: text/html
echo

cat << EOF

<HTML>

<meta http-equiv="Refresh" content="1; url=/">

</HTML>

