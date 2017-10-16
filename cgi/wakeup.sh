#!/bin/bash

# We set the default variables
startvolume="0"
endvolume="60"
fade="60" # The duration in seconds of the fading
changeplaylist="false"
random="false" # Toggles the random order
remote="false" # If true starts anyremote

remotecfg="$HOME""/Extra/Anyremote/Server-mode/mpd.cfg"
playlist="http://provisioning.streamtheworld.com/pls/KDFCFM.pls"

# We cycle through the options and modify the variables accordingly

echo "$remotecfg"

displayhelp() {
	echo "Usage: wakeup.sh [OPTIONS]..."
	echo "Starts MPD with a gentle fading, which is useful to wake up nicely."
	echo "It should be added to cron to wake up at a fixed time."
	echo "By default it activates random playing in MPD (see below)."
	echo ""
	echo -e "-s, --startvolume \t\t VOL sets the initial volume to VOL (default=20)"
	echo -e "-e, --endvolume VOL \t\t sets the final volume to VOL (default=80)"
	echo -e "-f, --fade TIME \t\t sets the fading duration to TIME seconds (default=150)"
	echo -e "-p, --playlist PLAYLIST \t before starting MPD, replaces the current playlist with PLAYLIST. If no PLAYLIST is given, it uses the default \"Sveglia\""
	echo -e "-r, --remote CFG \t\t before starting MPD, activates anyremote with the config file CFG. If no CFG is given, it uses the default \$HOME/Extra/Anyremote/Server-mode/mpd.cfg"
	echo -e "-n, --norandom \t\t\t deactivates the MPD random mode"
	echo -e "-h, --help \t\t\t displays this help and exits"
}

while [ "$1" != "" ]; do
	case "$1" in
		-h | --help )
			displayhelp
			exit;;
		-s | --startvolume )
			shift
			startvolume="$1"
			shift;;
		-e | --endvolume )
			shift
			endvolume="$1"
			shift;;
		-f | --fade )
			shift
			fade="$1"
			shift;;
		-p | --playlist )
			shift
			changeplaylist="true"
			if [ ! -z "$1" ] && [ "$(echo "$1" | cut -b 1 )" != "-" ]; then
				playlist="$1"
				shift
			fi;;
		-r | --remote )
			shift
			remote="true"
			if [ ! -z "$1" ] && [ "$(echo "$1" | cut -b 1 )" != "-" ]; then
				remotecfg="$1"
				shift
			fi;;
		-n | --norandom )
			shift
			random="false";;
		* )
			shift;;
		esac
done

deltavol=$[endvolume-startvolume]
echo "$deltavol"
step=$[fade/deltavol]

#if [ $changeplaylist = "true" ]; then
#set the playlist each time
mpc clear
mpc load "$playlist"
#fi

if [ $random = "true" ]; then
	mpc random on
else
	mpc random off
fi

if [ "$remote" = "true" ]; then
	anyremote -f "$remotecfg" &
fi

#mpc volume does not work
#mpc volume $startvolume
sudo amixer -q sset Headphone $startvolume

mpc play
i="0"
while [ "$i" -lt "$deltavol" ]; do
	sleep "$step"
	sudo amixer -q sset Headphone 1+
	i=$[i+1]
done
