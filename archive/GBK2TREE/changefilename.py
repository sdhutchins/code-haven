# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:34:58 2016

@author: shutchins2
"""
# Quick script designed to change file names and extensions easily on the MCSR.

import os
import sys
import csv

# Read a list of gene names from a .csv file.
g = open('Gene_1_names.csv')  # 1st column - gene names
file1 = csv.reader(g)

# Let me know where I am right before I start the loop.
print("\n" + "The current working directory is "+ os.getcwd() + (2 * "\n"))  # Print current working directory
Name_count = 0

for Name in file1:
    Name_count = Name_count + 1

    os.system("set -x")
    os.system("cp MASTER_" + str(Name[0]) + "_CDS.ffn.best " + str(Name[0]) + "_cds.fasta")
    os.system("rm -r MASTER_" + str(Name[0]) + "_CDS.ffn.best")

sys.exit("This script has completed.")