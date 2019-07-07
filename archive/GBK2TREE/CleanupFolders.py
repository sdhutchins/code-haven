# -*- coding: utf-8 -*-
"""

@author: S. Hutchins
"""
# Cleanup Folders

# List of modules used
import os
import sys
import csv

g = open('Gene_1_names.csv')  # 1st column - gene names
file1 = csv.reader(g)

# Let me know where I am right before I start the loop.
print("\n" + "The current working directory is "+ os.getcwd() + (2 * "\n"))  # Print current working directory
Gene_count = 0


for Gene in file1:
    Gene_count = Gene_count + 1

    # Assess current working directories and establishing home and output directories.
    a = '/ptmp/r2295/bin/Genes_1_CDS/' # Home directory
    home = a

    # Create directories for CDS files if they don't exist.
    os.chdir(home)  # Change to the home directory
    d = a + "./" + str(Gene[0])
    os.makedirs('%s' % d, exist_ok=True)

    os.chdir(d) # Change to cds.fasta file directory

    os.listdir() # Make a list of the files in the current directory

    print("➜ Current CDS/Gene directory: "+ os.getcwd() + "\n")  # Print current working directory

    input("If this is the desired directory, press ENTER.")
    print("\n")

    # Echos all commands in the current shell.
    os.system("set -x")

    # Remove the existing cds.fasta file before concatenation.
    os.system("rm -r " +  str(Gene[0]) + "_cds.fasta")
    print("\n")

    # Uses command line to concatenate fasta files in current directory.
    os.system("cat *_cds.fasta* > " + str(Gene[0]) + "_cds.fasta")
    print("\n")

    # Uses command line to remove "PREDICTED: " from beginning of lines in fasta file.
    os.system("sed -i 's/PREDICTED: //g' " + str(Gene[0]) + "_cds.fasta")
    print("\n")

    # Copy the cds.fasta file to a common directory.
    os.system("cp " + str(Gene[0]) + "_cds.fasta /ptmp/r2295/bin/NEWCDS")
    print("\n")

    # Remove the cds.fasta file
    os.system("rm -r " + str(Gene[0]) + "_cds.fasta")
    print("\n")


sys.exit("✓✓✓✓ This script has completed. ✓✓✓✓")  # Exit the script.