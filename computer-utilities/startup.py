# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:18:01 2016

@author: Shaurita D. Hutchins

Description: Startup certain files or programs. Set it on auto via command line.
"""
# Modules used
import os
from time import sleep
import logging as log
from datetime import datetime as d

#------------------------------------------------------------------------------
# Set up the logger
log.basicConfig(filename="startup.log", level=log.INFO)
log.info("#------------------------------------------------------------------")
log.info("The script name is %s" % os.path.basename(__file__))
log.info("The date and time is currently %s" % str(d.now()))

#------------------------------------------------------------------------------
# List the program paths if necessary. May be necessary if the default working
# directory of your command prompt does not include the programs.
spotify = r'C:\Users\shutchins2\AppData\Roaming\Spotify\Spotify.exe'
firefox = r'C:\"Program Files (x86)"\"Mozilla Firefox"\firefox.exe'
spyder = r'C:\Users\shutchins2\Desktop\Spyder.lnk'  # Shortcut link
winscp = r'C:\Users\shutchins2\Desktop\"Software & Executables"\WinSCP\WinSCP.exe'
putty = r'C:\Users\shutchins2\Desktop\"Software & Executables"\PUTTY\putty.exe'
slack = r'C:\Users\shutchins2\AppData\Local\slack\slack.exe'
outlook = 'OUTLOOK.EXE'
excel = 'EXCEL.EXE'
word = 'WINWORD.EXE'

# Make a list of the programs
programslist = [spotify, firefox, spyder, winscp, putty, slack, outlook,
                excel, word]

log.info("The programs I want to auto start are %s." % programslist)

#------------------------------------------------------------------------------
# Create a for loop that starts the programs using the os module.
for program in programslist:
    try:
        # The os.system() function uses Windows command prompt (cmd).
        os.system("start " + program)
        log.info("%s started." % program)
        sleep(1) # Take a short sleep as to not overwhelm the ram.
    except os.error:
        log.error("%s did not start." % program)

log.info("The end.") # let it be known that the script is ending

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
## Create an aspect of this program that takes input in the form of a path.
## From there it also takes a name of the program or file.
## Lastly it appends that program/file to the list before the for loop.
#
#listofprograms = input('What is the path of the program? ')
#path = listofprograms
#
#if path == programslist:
#    x = input('What is the common name of the program? ')
#    print('The common name is ' + x)
#else:
#    print('You did not enter a path.')
#    sys.exit('Bye.')

