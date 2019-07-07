# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 11:31:04 2016

Version 3.0

@author: Shaurita D. Hutchins

The current version of this program is designed for use on my local computer.
"""

# This script is designed to parse genbank files, extract the desired features,
# & store those features in fasta files or genbank files for downstream usage.


# List of modules used in this script
import sys
import time
import os
from Bio import SeqIO  # Used to parse .gbk files & extract record features.
import csv  # Read a comma delimited list.

# This prints a short description of the script.
print('#### This script is designed to parse genbank files and extract ' +
      'desired features. ###' + '\n')

# There are a few short "sleeps" in this program so that it can be completed
# interactively and read in real time.
time.sleep(.5)

# This is just a step to confirm that you are ready to start.
input("If you would like to start this script, press enter. ")
print("\n")

# Create and read a list of organisms from a .csv file.
org_list = []  # Initialize list of organisms
org_list.append('')
o = open('Organisms.csv')  # Open a comma delimited list of organisms.
file1 = csv.reader(o)
for org in file1:  # Format a list of organisms
    org = str(org)
    org = org.replace("'", "")
    org = org.replace("[", "")
    org = org.replace("]", "")
    org = org.replace(" ", "_")
    org_list.append(org)
print("List of Organisms" + "\n")
print(org_list)  # Print the list of organisms
time.sleep(0.5)

g = open('Gene_1_names.csv')  # 1st column - gene names
file2 = csv.reader(g)

# Let me know where I am right before I start the loop.
print("\n" + "The current working directory is " +
      os.getcwd() + (2 * "\n"))  # Print current working directory
time.sleep(.5)
Gene_count = 0

# Loop to create gene directories. This loop includes 2 other loops. Be
# mindful.
for Gene in file2:
    Gene_count = Gene_count + 1

    # Assess current working directories and establishing home and output
    # directories.

    a = r'C:\Users\shutchins2\Desktop\In Progress\Code\GBK2TREE\GBK'  # Home directory
    home = a  # Location of genbank directories and files
    b = r'C:\Users\shutchins2\Desktop\In Progress\Code\GBK2TREE\CDS'  # Output directory
    output = b  # Location of cds.fasta files
    os.chdir(output)  # Directory change to output directory

    # Create directories for CDS/Fasta files.
    c = b + "./" + str(Gene[0])
    # Create a directory or don't if it exists.
    os.makedirs('%s' % c, exist_ok=True)

    # Create directories for Genbank files.
    os.chdir(home)  # Change to the home directory
    d = a + "./" + str(Gene[0])
    os.makedirs('%s' % d, exist_ok=True)

    os.chdir(d)  # Change to genbank file directory
    os.listdir()  # Make a list of the files in the current directory
    # Print current working directory
    print("➜ Current gene directory: " + os.getcwd() + "\n")
    time.sleep(.3)
    input("    If this is the desired directory, press ENTER.")
    print("\n")

# -----------------------------------------------------------------------------

# Parse genbank files & write CDS to 1 fasta file per gene for multipl
    time.sleep(.3)
    file_count = 0
    # Loop that establishes organism list, reads genbank file, and
    # creates/opens new fasta file.
    for Organism in org_list:
        file_count = file_count + 1
        maximum = 0
        if Organism == '':
            continue
        os.chdir(d)  # Directory of genbank files
        record = SeqIO.read(str(Gene[0]) + "_" + Organism + ".gbk", "genbank")
        os.chdir(c)  # Change to directory for cds.fasta files
        # You can also create a genbank file.
        output_handle = open(str(Gene[0]) + "_" + Organism + "_cds.fasta", "w")
        count = 0
        # Loop that extracts specific features and writes them to previously
        # created file.
        for feature in record.features:
            # Other annotated features are 'Gene', 'mRNA', 'CDS', and 'ncRNA'.
            if feature.type == "CDS":
                count = count + 1
                # Use record.dbxrefs here. Look up record features in Ipython
                # using 'dir(record)'.
                feature_name = (Organism)
                feature_seq = feature.extract(record.seq)
                # Simple FASTA output without line wrapping:
                output_handle.write(">" + feature_name +
                                    "\n" + str(feature_seq) + "\n")
                output_handle.close()
                print(Organism + "\n" + feature_name + "\n" + feature_seq +
                      "\n" + "\n" + str(count) +
                      " CDS sequence was extracted from " + Organism + "." +
                      (2 * "\n"))
                # time.sleep(0.15)
        print((100 * "#") + "\n" + (100 * "#") + "\n" +
              (100 * "#") + "\n")  # Creating space between output
        print(2 * "\n")
    print((50 * "★") + "\n")
    # This input lets you know which gene is next.
    input("If you would like to continue to the next gene, press ENTER. ")
    print("\n")

print("This script has finished. ✓ You may exit now.")
o.close()
g.close()
sys.exit()
