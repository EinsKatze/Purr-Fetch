#!usr/bin/python3
# -- welcome to this bloated mess --

from os import environ
from datetime import timedelta

# shell
shell = environ['SHELL']  # /bin/bash

# uptime
with open("/proc/uptime", "r") as uptime:
    time = float(uptime.read().split(" ")[0])
    uptime = timedelta(seconds=time)

# hostname
with open("/etc/hostname", "r") as host:
    # With blocks ensure that the file will get closed
    hostname = host.read().strip()

# distro
with open("/etc/issue", "r") as distro:
    distrob = distro.read().strip().replace("(\\l)", "").replace("\r", "").replace("\n", "")

# kernel
with open("/proc/sys/kernel/ostype", "r") as ostype:
    with open("/proc/sys/kernel/osrelease", "r") as osrelease:
        kernel = ostype.read().replace("\n", " ") + osrelease.read().replace("\n", "")

def structure():
    print()
    print("(\\_/) \033[0;33m     uptime:      %s\033[0;0m" % (uptime))  # orange
    print("(oᴥo) \033[0;31m     shell:       %s\033[0;0m" % (shell))  # red
    print("|U°U| \033[0;35m     distro:      %s\033[0;0m" % (distrob))  # purple
    print("|   | \033[0;34m     hostname:    %s\033[0;0m" % (hostname))  # blue
    print("'U_U' \033[0;36m     kernel:      %s\033[0;0m" % (kernel))  # cyan
    print("  U")  


structure()
