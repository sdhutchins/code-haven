# -*- coding: utf-8 -*-
"""
Last updated on November 21, 2016

@author: Shaurita D. Hutchins
"""

# This script is designed to clean a .csv file filled with accession numbers and validate those accession numbers.

# List of modules used
import pandas as pd
import os
import csv

# Designate the directory of the file I'm using
home = r'C:\Users\shutchins2\Desktop'

# Change to the home directory
os.chdir(home)

# Open a .csv file that contains 1 column of organism names
# Make a list of organisms and use it for column headers in the master file
org_list = []   # Initialize a list of organisms
org_list.append('')
o = open('Organisms.csv')
file2 = csv.reader(o)
for org in file2:    # Format a list of organisms
    org = str(org)
    org = org.replace("'", "")
    org = org.replace("[", "")
    org = org.replace("]", "")
    org = org.replace(" ", "_")
    org_list.append(org)
print(org_list)

########################################################################################################################
# Using Pandas to read existing .csv files

#Use the pandas module to read this .csv file
df = pd.read_csv('MAF.csv')

# Replace NaN or empty cells with a space
df = df.fillna('n/a')

for Organism in org_list:
        Org = str(Organism)
        x = "df." + Org
        print(x)

        # Blastdbcmd in Linux shell
        os.system("blastdbcmd -db refseq_rna -entry "  + ACC + " -outfmt % t")



