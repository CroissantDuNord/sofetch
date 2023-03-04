#!/usr/bin/env python3

from os import system
from os import name as os_name
from sys import platform as sys_platform
from socket import gethostname as hostname
from platform import platform as os_platform
from platform import machine as machine_platform
from cpuinfo  import get_cpu_info as cpu_info
import distro as dist
from psutil import virtual_memory, boot_time
from datetime import datetime, date
from ascii import *

SOFETCH_VERSION = '0.0.1'

hostUsername    = hostname()
osPlatform      = os_platform()
machinePlatform = machine_platform()
cpuInfo         = cpu_info()['brand_raw']
memory           = round(virtual_memory().total / (1024.0 ** 3), 2)
dateToday       = date.today()
upTime          = datetime.fromtimestamp(boot_time()).strftime("%Y-%m-%d %H:%M:%S")

def sofetch():

    if "Manjaro" in dist.name():
        print(manjaro)
    elif "Fedora" in dist.name():
        print(fedora)
    elif "Ubuntu" in dist.name():
        print(ubuntu)
    elif "Debian" in dist.name():
        print(debian)
    elif "Gentoo" in dist.name():
        print(gentoo)
    elif "Arch" in dist.name():
        print(arch)
    elif "Mint" in dist.name():
        print(mint)
    elif "Lite" in dist.name():
        print(lite)
    elif "Garuda" in dist.name():
        print(garuda)
    elif sys_platform.startswith('linux'):
        print(linux)
    elif "Windows-10" in osPlatform:
        print(win10)
    elif "Windows-11" in osPlatform:
        print(win11)
    elif "Windows-8.1" in osPlatform:
        print(win10)
    elif "Windows-8" in osPlatform:
        print(win10)
    elif "Windows-7" in osPlatform:
        print(win7)
    elif "Windows-Vista" in osPlatform:
        print(win7)
    elif "Windows-XP" in osPlatform:
        print(windows)
    elif "Mac" in osPlatform:
        print(macos)
    elif "mac" in osPlatform:
        print(macos)
    else:
        print(unknown)

    print(f'[bold magenta] Username\t\t~> {hostUsername} [/bold magenta]')
    print(f'[bold magenta] Date\t\t\t~> {dateToday} [/bold magenta]')
    print(f'[bold magenta] OS\t\t\t~> {osPlatform} [/bold magenta]')
    print(f'[bold magenta] Uptime\t\t\t~> {upTime} [/bold magenta]')
    print(f'[bold magenta] Memory\t\t\t~> {memory} GB [/bold magenta]')
    print(f'[bold magenta] CPU\t\t\t~> {cpuInfo} [/bold magenta]')
    print(f'[bold magenta] Machine Platform\t~> {machinePlatform} [/bold magenta]\n')
    print(f'[bold green] Sofetch version: {SOFETCH_VERSION} [/bold green]')

sofetch()
