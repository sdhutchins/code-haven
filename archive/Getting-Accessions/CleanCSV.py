# -*- coding: utf-8 -*-
"""
Last updated on November 7, 2016

@author: Shaurita D. Hutchins
"""

# This script is designed to remove duplicates from a .csv file and not which duplicates were removed in a .txt file.

#------------------------------------------------------------------------------
# List of modules used.
#------------------------------------------------------------------------------

import pandas as pd

#------------------------------------------------------------------------------
# Use pandas to read in the dataframe and create lists.
#------------------------------------------------------------------------------


f1 = pd.read_csv('MAFV3.1.csv', index_col=False, dtype=str)
master = pd.DataFrame(f1) # Get the keys - master.keys()

# Set keys as variables
genes = list(master['Gene']) # All genes
tiers = list(master['Tier']) # All tiers of genes

# Create tier lists
tier1 = []
tier2 = []
tier3 = []
notier = []
for gene, tier in zip(genes, tiers):
    if tier == '1':
        tier1.append(gene)
    if tier == '2':
        tier2.append(gene)
    if tier == '3':
        tier3.append(gene)
    if tier == 'None':
        notier.append(gene)

tierlist = [tier1, tier2, tier3, notier]