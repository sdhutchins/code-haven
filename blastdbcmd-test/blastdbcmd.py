# -*- coding: utf-8 -*-
"""
Date created: Thu Mar 30 22:35:23 2017
Author: S. Hutchins

Description: Test that checks whether the accession number is in the blastdb.

"""
# Modules used
import pandas as pd
import subprocess
import os
import logging as log
from datetime import datetime as d

#------------------------------------------------------------------------------
# Create a directory for the fasta files
os.mkdir('fasta-files')

# Set up the logger
log.basicConfig(filename="accessions2blastxml.log", level=log.INFO)
log.info("#------------------------------------------------------------------")
log.info("The script name is %s" % os.path.basename(__file__))
log.info("The date and time is currently %s" % str(d.now()))

# Create lists
found_genes =[]  # This will set up a list of genes in the blastdb
unfound_genes = []  # This will set up a list of genes NOT in the blastdb

# Import the csv file that has the preselected genes/accessions
file = pd.read_csv('accs.csv', header=None)
genes = list(file[0])  # This is a list of the genes in column 1
accs = list(file[1])  # This is a list of the accession #'s in column 2

#------------------------------------------------------------------------------
# This for loop iterates through a zipped list to test if the entry is in the db.
# It uses the 'blastdbcmd'. You must have the NCBI standalone executables.
for acc, gene in zip(accs, genes):    
    # Create a temporary fasta file since the blastn command needs a sequence file as input.
    cmd = "blastdbcmd -entry " + acc +" -db refseq_rna -outfmt %f -out fasta-files/HUMAN_" + gene + ".fasta"
    result = subprocess.call([cmd], shell=True)
    
    if result == 0:  # Command was successful. Entry was found.
        found_genes.append(gene)
        
    else:  # Command was unsuccessful. Stdout will be '1'. Entry was NOT found.
        unfound_genes.append(gene)
        os.system("rm -r fasta-files/HUMAN_" + gene + ".fasta")
        continue
    
#------------------------------------------------------------------------------
# Turn the lists into dataframes and save as csv files
norecord = pd.DataFrame(unfound_genes)
norecord.to_csv('genes_not_found.csv', header=None, index=False)
record = pd.DataFrame(found_genes)
record.to_csv('genes_found.csv', header=None, index=False)
log.info("Your csv files have been created and saved.")

# Log how many genes there are and how many were or weren't in the blastdb
log.info("There are %s total genes." % len(genes))
log.info("There were %s genes found in the refseq_rna blastdb." % len(found_genes))
log.info("There were %s genes NOT found in the refseq_rna blastdb." % len(unfound_genes))