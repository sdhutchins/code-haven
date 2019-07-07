# -*- coding: utf-8 -*-
"""
Last updated on November 16, 2016

@author: Shaurita D. Hutchins

"""
# List of modules used
from subprocess import call
import os

dirlist = os.popen('ls -l').read()
print(dirlist)

call('ls') # Calls a specific command from the command line
os.remove('file name')  # Removes a file from the current shell