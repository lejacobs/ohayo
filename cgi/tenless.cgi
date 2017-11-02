#! /bin/bash
sudo amixer -q sset Headphone 10-
echo Content-type: text/html
echo

cat << EOF

<HTML>

<meta http-equiv="Refresh" content="1; url=/">

</HTML>
