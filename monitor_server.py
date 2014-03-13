#!/usr/bin/python

__author__ = 'sumit'

import subprocess
from subprocess import Popen, PIPE, call
from time import gmtime, strftime

time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
out = "------------------------------------------------ Start: " + time + "---------------------------------------------- \n"

out += "-------------- Process List --------------\n"
process = Popen(["ps", "aux"], stdout=PIPE)
out += process.communicate()[0]
process.stdout.close()

out += "\n-------------- CPU usage - [TOP] --------------\n"
#top = subprocess.call("top -n 1 -b", shell=True)
top = Popen(["top", "-n", "1", "-b"], stdout=PIPE)
out += top.communicate()[0]
top.stdout.close()

out += "\n-------------- Memory Usage --------------\n"
#free =  subprocess.call("free -m", shell=True)
free = Popen(["free", "-m"], stdout=PIPE)
out += free.communicate()[0]
free.stdout.close()

time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
out += "\n------------------------------------------------ End: " + time + "----------------------------------------------\n"
print out
