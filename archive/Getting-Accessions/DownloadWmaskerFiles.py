# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 09:54:37 2016

@author: Shaurita D. Hutchins
"""
# This script is designed to create directories for taxonomy id databases on
# the MCSR and download databases (obinary files) into directories.

# List of modules used.
import os
import csv
import sys

# Open taxids.csv which is a comma delimited list of all tax id's to be used.
taxid = open('taxids.csv')  # 1st column - tax id's
file1 = csv.reader(taxid)
TaxID_count = 0

# Main "for" loop in this file that creates directories & downloads files.
for ID in file1:
    TaxID_count = TaxID_count + 1

    # Create taxonomy id windowmasker file directories.
    a = '/home/ums/r2295/bin/Orthologs-Project/'  # Home Directory
    home = a  # Location of taxids.csv file
    b = '/ptmp/r2295/bin/Mask/'  # Output directory
    output = b  # Location of obinary directories/files
    os.chdir(output)  # Directory Change: Output directory

    # Create directories for windowmasker obinary files.
    c = b + "./" + str(ID[0])
    os.makedirs('%s' % c, exist_ok=True)  # Create directory if it doesn't exist.
    os.listdir()  # Make a list of the files in the current directory
    os.chdir(c)

    # Print the current working directory
    print("The current working directory is " + os.getcwd())

    # Use NCBI's FTP service to locate files and download them.
    os.system("ftp ftp://ftp.ncbi.nih.gov/blast/windowmasker_files/" + str(ID[0]) + "/wmasker.obinary")
    print("The directory and file for " + str(ID[0]) + " have been created.")

sys.exit("Done! ✓")
