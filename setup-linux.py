import distro as dist
import sys
import os

print("Hello and Welcome to the installer for sofetch")
print("Have you downloaded the repo locally [y/n]")
input = input()
if input == "y":
    print("Provide full path to the root of the repository (with the slash):")
    inputrepo = input()
    if "Manjaro" in dist.name():
        os.system("sudo pacman -S python3 python-pip")
    elif "Fedora" in dist.name():
        os.system("sudo dnf install python3 python3-pip")
    elif "Ubuntu" in dist.name():
        os.system("sudo apt install python3 python-pip")
    elif "Debian" in dist.name():
        os.system("sudo apt install python3 python-pip")
    elif "Gentoo" in dist.name():
        os.system("sudo emerge --ask dev-lang/python:3.10")
        os.system("sudo emerge --ask dev-python/pip")
    elif "Arch" in dist.name():
        os.system("sudo pacman -S python3 python-pip")
    elif "Mint" in dist.name():
        os.system("sudo apt install python3 python-pip")
    elif "Lite" in dist.name():
        os.system("sudo apt install python3 python-pip")
    elif "Garuda" in dist.name():
        os.system("sudo pacman -S python3 python-pip")
    os.system("pip install --use-pep517 -r ", inputrepo, "requirements.txt && sudo mv ", inputrepo, "sofetch/* /usr/bin/ && sudo mv /usr/bin/sofetch.py /usr/bin/sofetch && sudo chmod +x /usr/bin/sofetch")
    print("done..")
elif input == "n":
     print("Ok dont worry we will do some things to get it ready")
     if "Manjaro" in dist.name():
        os.system("sudo pacman -S git python3 python-pip")
    elif "Fedora" in dist.name():
        os.system("sudo dnf install git python3 python3-pip")
    elif "Ubuntu" in dist.name():
        os.system("sudo apt install git python3 python-pip")
    elif "Debian" in dist.name():
        os.system("sudo apt install git python3 python-pip")
    elif "Gentoo" in dist.name():
        os.system("sudo emerge --ask dev-lang/python:3.10")
        os.system("sudo emerge --ask dev-python/pip")
        os.system("sudo emerge --ask dev-vcs/git")
    elif "Arch" in dist.name():
        os.system("sudo pacman -S git python3 python-pip")
    elif "Mint" in dist.name():
        os.system("sudo apt install git python3 python-pip")
    elif "Lite" in dist.name():
        os.system("sudo apt install git python3 python-pip")
    elif "Garuda" in dist.name():
        os.system("sudo pacman -S git python3 python-pip")
    os.system("cd /tmp && git clone --recursive https://github.com/Soviet-Linux/sofetch && pip install --use-pep517 -r requirements.txt && sudo mv /tmp/sofetch/sofetch/* /usr/bin/ && sudo mv /usr/bin/sofetch.py /usr/bin/sofetch && sudo chmod +x /usr/bin/sofetch && rm -rf /tmp/sofetch/ && cd ~")
    print("done..")
