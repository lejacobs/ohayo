#! /usr/bin/env python

import cgi
import cgitb; cgitb.enable() # Optional; for debugging only
from subprocess import call

print "Content-Type: text/html"
print
print """\
<html>
<meta http-equiv="Refresh" content="1; url=/">
</HTML>
"""

cronfilename = "/usr/lib/cgi-bin/openDir/cronwake.txt"

f = open(cronfilename, 'w')

arguments = cgi.FieldStorage()
waketime = arguments["wake"].value
params = waketime.split(':')
minute = params[1]
hour = params[0]

f.write(minute)
f.write(" ")
f.write(hour)
f.write(" * * * /usr/lib/cgi-bin/wakeup.sh\n") 

f.close()

call(["crontab", cronfilename])
