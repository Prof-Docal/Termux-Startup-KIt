#!/bin/python

import os
import sys
import shutil





if os.path.exists('/data/data/com.termux/files'):
    pass
else:
    if os. geteuid() != 0: 
        exit("You need to have root privileges to run this script.")
        sys.exit()


inp=input('Are You Sure To Uninstall Termux-Startup-Kit ? (yes/no) = ')
if inp.lower()=='yes' or inp.lower()=='y':
    if os.path.exists('/data/data/com.termux/files'):
        INSTALL_DIR="$PREFIX/usr/share/doc/Termux-Startup-Kit"
        BIN_DIR="$PREFIX/usr/bin/"
        
    else:
        INSTALL_DIR="/usr/share/doc/Termux-Startup-Kit"
        BIN_DIR="/usr/bin/"
    print('Deleting `'+BIN_DIR+'Termux-Startup-Kit` File')
    try:
        os.remove(BIN_DIR+'Termux-Startup-Kit')
        
    except:
        print('Application Couldn\'t uninstall , make sure you have proper permission or reinstall it again to uninstall')
        sys.exit()


    print('Deleting `'+INSTALL_DIR+'` Folder')
    try:
        shutil.rmtree(INSTALL_DIR)
    except:
        print('Application Couldn\'t uninstall , make sure you have proper permission or reinstall it again to uninstall')
        sys.exit()
    
    print('Uninstall Success!')


else:
    print('Uninstall Canceled! ')
