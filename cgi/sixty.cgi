#! /bin/bash
sudo /usr/bin/amixer -q sset Headphone 60
echo Content-type: text/html
echo

cat << EOF

<HTML>

<meta http-equiv="Refresh" content="1; url=/">

</HTML>
