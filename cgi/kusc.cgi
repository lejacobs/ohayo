#! /bin/bash
echo -e "Location: http://ohayo/index.html\n\n"
mpc stop
mpc clear
mpc load http://playerservices.streamtheworld.com/pls/KUSCMP128.pls
mpc play
mpc status
