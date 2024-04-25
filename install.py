import os

os.system("clear")

print("  _______                                _____ _             _                 _  ___ _     ")
print(" |__   __|                              / ____| |           | |               | |/ (_) |    ")
print("    | | ___ _ __ _ __ ___  _   ___  __ | (___ | |_ __ _ _ __| |_ _   _ _ __   | ' / _| |_   ")
print("    | |/ _ \ '__| '_ ` _ \| | | \ \/ /  \___ \| __/ _` | '__| __| | | | '_ \  |  < | | __|  ")
print("    | |  __/ |  | | | | | | |_| |>  <   ____) | || (_| | |  | |_| |_| | |_) | | . \| | |_   ")
print("    |_|\___|_|  |_| |_| |_|\__,_/_/\_\ |_____/ \__\__,_|_|   \__|\__,_| .__/  |_|\_\_|\__|  ")
print("                                                                      | |                   ")
print("                                                                      |_|                   ")
print
print("                   <===============Created By Prof Docal===============>")
print

print("UPDATING AND UPGRADING TERMUX PACKAGES...")
os.system("apt update")
os.system("apt upgrade")
os.system("pkg update")
os.system("pkg upgrade")
print("UPDATES AND UPGRADES COMPLETED!")
print

print("SETTING UP TERMUX STORAGE...")
os.system("termux-setup-storage")
print("SETUP DONE!")
print

print("INSTALLING TERMUX STARTUP PACKAGES...")
os.system("apt install git")
os.system("apt install nano")
os.system("apt install wget")
os.system("apt install openssh")
os.system("pkg install python")
os.system("pkg install python2")
os.system("pkg install python3")
os.system("pkg install python-pip")
os.system("pkg install php")
os.system("apt install curl")
os.system("apt install clang")
os.system("apt install neovim")
os.system("apt install apache2")
os.system("pkg install cmatrix")
os.system("apt install zip")
os.system("apt install unzip")
print("TERMUX STARTUP PACKAGES INSTALLATION DONE!")
print

print("Thank you for using my program.")
print("Termux is Up and Ready to go!!!")
