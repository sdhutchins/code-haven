# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 13:31:08 2016

@author: Shaurita D. Hutchins
"""

# This script is designed to create a gi list based on the refseq_rna database
# for each taxonomy id on the MCSR. It will also convert the gi list into a 
# binary file which is more efficient to use with NCBI's Blast tools.

# List of modules used.
import os
import csv
import sys

# Mark start of program with printed text.
print("\n" + (90 * "#") + "\n" + "Create a GI list for each organism using the \
taxonomy id and the blastdbcmd tool on the MCSR.  ####" + "\n" + (90 * "#") + "\n")

# Open taxids.csv which is a comma delimited list of all tax id's to be used.
taxid = open('taxids.csv')  # 1st column = tax id's
file1 = csv.reader(taxid)
TaxID_count = 0

# Main "for" loop in this file that creates gi list files in binary format in the current/home directory.
for ID in file1:
    TaxID_count = TaxID_count + 1

    a = '/home/ums/r2295/bin/Orthologs-Project/'  # Home Directory
    home = a  # Location of taxids.csv
    os.chdir(home)  # Directory Change: Output directory

    # Use a list of accession #'s and the blastdbcmd tool to generate gi lists.
	# The entry/entries should be accession numbers.
    os.system("blastdbcmd -db refseq_rna -entry all -outfmt '%g %T' | awk ' { if ($2 == " + str(ID[0]) + ") { print $1 } } ' > " + str(ID[0]) + "gi.txt")
    print(str(ID[0]) + "gi.txt" + " has been created.")

    # Convert the .txt file to a binary file using the blastdb_aliastool.
    os.system("blastdb_aliastool -gi_file_in " + str(ID[0]) + "gi.txt -gi_file_out " + str(ID[0]) + "gi")
    print(str(ID[0]) + "gi binary file has been created.")

    # Remove the gi.text file
    os.system("rm -r *gi.txt")

    # Move the gi file to a folder
    os.system("mv " + str(ID[0]) + "gi GiLists/")


sys.exit("The script has completed! ✓")
