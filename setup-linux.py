import distro as dist
import sys
import os

print("Hello and Welcome to the installer for sofetch")
print("Have you downloaded the repo locally [y/n]")
input = input()
if input == "y":
     print("Provide full path to the root of the repository:")
     inputrepo = input()
     os.system("sudo mv ", inputrepo, "sofetch/* /usr/bin/")
     print("done reload your terminal")
elif input == "n":
     print("Ok dont worry we will do some things to get it ready")
     if "Manjaro" in dist.name():
        os.system("sudo pacman -S git python3 python-pip")
    elif "Fedora" in dist.name():
        os.system("sudo dnf install git python3 python3-pip")
    elif "Ubuntu" in dist.name():
        os.system("sudo apt install python3 python-pip")
    elif "Debian" in dist.name():
        os.system("sudo apt install python3 python-pip")
    elif "Gentoo" in dist.name():
        os.system
    elif "Arch" in dist.name():
        print(arch)
    elif "Mint" in dist.name():
        print(mint)
    elif "Lite" in dist.name():
        print(lite)
    elif "Garuda" in dist.name():
        print(garuda)
#NOT READY 
