# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 12:05:48 2016

@author: shutchins2
"""
# Integrate subprocess module with Orthophylip.py script for phylip.exe on MCSR

import shlex, subprocess

command_line = input('spotify.exe')
args = shlex.split(command_line)
print(args)
p = subprocess.Popen(args)