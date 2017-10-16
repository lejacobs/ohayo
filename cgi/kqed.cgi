#! /bin/bash
echo -e "Location: http://ohayo/index.html\n\n"
mpc stop
mpc clear
mpc load http://streams.kqed.org/kqedradio.m3u
mpc play
mpc status
