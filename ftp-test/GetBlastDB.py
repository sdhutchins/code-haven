# -*- coding: utf-8 -*-
"""
Description: This script downloads the refseq_rna blast db files. Check the
ReadMe file for a first time setup of a blast database.

@author: Shaurita Hutchins
Date Created: Tue Feb 28 19:05:41 2017
Project Name: GPCR Orthologs Project
"""

# Modules used
from ftplib import FTP, error_perm
import os
import fnmatch
import sys
import logging as log
from datetime import datetime as d

# Set up the logger for logging
# Set up the logger
log.basicConfig(filename="getblastdb.log", level=log.INFO)
log.info("#------------------------------------------------------------------")
log.info("The script name is %s" % os.path.basename(__file__))
log.info("The date and time is currently %s" % str(d.now()))

#------------------------------------------------------------------------------
# Create a directory for the database if one doesn't exist
dbpath = 'databases/refseq_rna_db'  # This will be a subdirectory in your current folder
try:
    # If the directory exists,
    if os.path.exists(dbpath) == True:
        log.info("The %s directory exists & will be archived." % str(dbpath))
        # Move any files that are in the directory to a dated archive folder.
        os.system("alias logdate='date +%m-%d-%y@%I:%M-%p'; logname=$(logdate)")
        # Moving a directory in linux/unix essentially renames it.
        os.system('mv ' + dbpath + ' refseqrnadb_archive_$logname')
        os.mkdir(dbpath)   # Recreate the database directory
        log.info("The %s directory was created." % str(dbpath))
        pass
    else:  # If the directory does not exist
        os.mkdir(dbpath)
        log.info("The %s directory was created." % str(dbpath))
except os.error:
    log.info("Error.")
    sys.exit("There has been an error.")

os.chdir(dbpath)  # Change to the database directory

#------------------------------------------------------------------------------
# Connect to the NCBI ftp site
try:
    ncbi = 'ftp.ncbi.nlm.nih.gov/'
    blastdb = '/blast/db/'  # Set variable for the blastdb subdirectory
    ftp = FTP("ftp.ncbi.nlm.nih.gov", timeout=None)
    # Login using email as password
    ftp.login(user='anonymous', passwd='shutchins2@umc.edu')
    log.info("Successful FTP login.")
except error_perm:  # This error will be thrown if there's a connection issue.
    log.info("FTP connection error.")
    sys.exit()

# Change to the desired directory
ftp.cwd(blastdb)
# Use ftp.pwd() to find out the current directory
# Use ftp.retrlines('LIST') to get a list of all the files in the directory

# This is a list of the file names in the current directory
filenames = ftp.nlst()

#------------------------------------------------------------------------------
# Create a for loop that writes the list/text file of files wanted
with open('refseqrna-downloadlist.txt', 'w') as refseq:
    for filename in filenames:
        if fnmatch.fnmatch(filename, 'refseq_rna*'):  # Get only those files.
            host_file = os.path.join(filename)
            # Write the url of each refseq_rna db file to a text file.
            refseq.writelines(ncbi + blastdb + host_file + '\n')

# Download the list of files using 'wget' on linux/unix
try:
    os.system('cat refseqrna-downloadlist.txt | xargs -n 1 -P 8 wget')
    log.info("The refseqrna blast db files have downloaded.")
except os.error:
    log.info("There has been an error.")
    sys.exit()
    ftp.quit()

ftp.close()

#------------------------------------------------------------------------------
# Unzip all of the files and remove unneccessary files
os.system('rm -r *.md5')  # Remove files with .md5 extension
os.system('gunzip *.gz')  # Unzip the database files
log.info("The files have been unzipped, and the script has finished.")
log.info("#------------------------------------------------------------------")
