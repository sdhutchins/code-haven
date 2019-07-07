# -*- coding: utf-8 -*-
"""
Created on Sat Sep 3 12:45:53 2016

@author: Shaurita D. Hutchins
"""
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################

# List of all modules used in this script. Make sure you have all of these installed.
# import time
# import os
# from Bio import SeqIO
# from Bio.Align.Applications import ClustalOmegaCommandline
# import csv #Read a comma delimited excel file.


# Providing a description of the script so that the user can understand what's happening.

describe_script = "#### This script is designed to extract features from genbank files, save those features as fasta files, align specific features such as coding sequences by gene across species, and create a phylogenetic tree. ####"
print("\n" + describe_script + "\n")

input("If you would like to continue, press ENTER. ")
print("\n")

# Just a little fun. Hehe.
import time
import os
print("(•_•)" + "\n")
time.sleep(.75)
os.system("cls")
print("( •_•)>⌐■-■" + "\n")
time.sleep(.75)
os.system("cls")
print("(⌐■_■)")
time.sleep(.75)
print("\n" + "Let's GEAUX!!!!" + (2 * "\n"))
time.sleep(.75)
print((107 * "#") + "\n" + (107 * "#") + "\n" + (107 * "#") + (3* "\n"))
time.sleep(.75)


##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################


# Listing of modules that will be used in loop(s).
from Bio import SeqIO #Downstream usage of this module for parsing genbank files & extracting record features.
#from Bio.Align.Applications import ClustalOmegaCommandline #Used to align multiple sequences within a fasta file.

# Assessing current working directories and establishing home and output directories.
print("The current working directory is -->  "+ os.getcwd() + "\n")  # Print current working directory
time.sleep(0.5)

import csv # Read list of files.
org_list = []  # Initialize the list of organisms.
org_list.append('')
o = open('Organisms.csv')
file1 = csv.reader(o)
for org in file1:    # Format the list of organisms.
    org = str(org)
    org = org.replace("'", "")
    org = org.replace("[", "")
    org = org.replace("]", "")
    org = org.replace(" ", "_")
    org_list.append(org)
print(org_list)
time.sleep(0.5)

g = open('Gene_names.csv')  ## 1st column - gene names
file2 = csv.reader(g)

Gene_count = 0

for Gene in file2:
    Gene_count = Gene_count + 1


    a = 'C:/Users/shutchins2/Desktop/In Progress/Code/GBK2TREE/GBK' #Home Directory
    home = a  # Location of genbank directories and files
    b = 'C:/Users/shutchins2/Desktop/In Progress/Code/GBK2TREE/CDS'  # Output directory of cds.fasta files
    output = b
    os.chdir(output)  # Directory Change: Output directory

    # Create directories for CDS/Fasta files.
    c = b + "./" + str(Gene[0])
    os.makedirs('%s' % c, exist_ok=True)  # Create directory or don't if it exists.

    # Create directories for Genbank files.
    os.chdir(home)  ## Make a list of files
    d = a + "./" + str(Gene[0])
    os.makedirs('%s' % d, exist_ok=True)

    os.chdir(d)  # Change to genbank file directory
    os.listdir()  # Make a list of the files in the current directory


##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################


##### Part 1: Parse genbank files & write CDS to 1 fasta file per gene for multiple alignments. #####
    time.sleep(1)
    file_count = 0
    for Organism in org_list:
        file_count = file_count + 1
        maximum = 0
        if Organism == '':
            continue
        os.chdir(d) # Directory of genbank files
        record = SeqIO.read(str(Gene[0]) + "_" + Organism + ".gbk", "genbank") #This is all flubbed up!

        os.chdir(c) #Change to directory for cds.fasta files
        output_handle = open(str(Gene[0]) + "_" + Organism + "_cds.fasta", "w")
        count = 0
        for feature in record.features:
            if feature.type == "CDS": # Other annotated features are 'Gene', 'mRNA', 'CDS', and 'ncRNA'.
                count = count + 1
                feature_name = (record.name + ":" + record.description) # Use record.dbxrefs here. Look up record features in Ipython using 'dir(record)'.
                feature_seq = feature.extract(record.seq)
                # Simple FASTA output without line wrapping:
                output_handle.write(">" + feature_name + "\n" + str(feature_seq) + "\n")
                output_handle.close()
                print(feature_name + "\n" + feature_seq + "\n" + "\n" + str(count) + " CDS sequence was extracted from "+ Organism + "." + (2 * "\n"))
                #time.sleep(0.15)
    print((107 * "#") + "\n" + (107 * "#") + "\n" + (107 * "#") + (3* "\n"))

     # Add this at some point.
#    input("If you would like to continue to the next gene, press ENTER. ")
#    print(2 * "\n")

###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
#
#
##Part 2: Align fasta files using Clustal Omega via MCSR.
#
#    print("\n" + "#### Part 2: Align fasta files using Clustal Omega via MCSR. ####" + "\n")
#
#    os.system("set -x") # For the current shell, echos all commands.
#    os.system("cat *_cds.fasta* > " + str(Gene[0] + ".fasta")) # Use command line to concatenate fasta files in current directory.
#
##Create a definition or not?
##def clustalo():
##    in_file = str(Gene[0]) + "_cds.fasta"
##    out_file = str(Gene[0]) + "_cds_aligned.fasta"
##    clustalomega_cline = ClustalOmegaCommandline(infile=in_file, outfile=out_file, verbose=True, auto=True)
##    print(clustalomega_cline)
##clustalo()
#
#    in_file = str(Gene[0]) + "_cds.fasta"
#    out_file = str(Gene[0]) + "_cds_aligned.aln"
#    clustalomega_cline = ClustalOmegaCommandline(infile=in_file, outfile=out_file, outfmt="clustal", verbose=True, auto=True)
#    print(clustalomega_cline)
#
#    in_file2 = str(Gene[0]) + "_cds.fasta"
#    out_file2 = str(Gene[0]) + "_cds_aligned.phylip"
#    clustalomega_cline2 = ClustalOmegaCommandline(infile=in_file2, outfile=out_file2, outfmt="phylip", verbose=True, auto=True)
#    print(clustalomega_cline2)