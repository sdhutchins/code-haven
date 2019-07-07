# -*- coding: utf-8 -*-
"""
Date created: Fri Mar 31 03:43:29 2017
Author: S. Hutchins

Description: Get tax ids and common names using the Entrez Api.

"""
import pandas as pd
from Bio import Entrez
from time import sleep as pause

orgs = pd.read_csv('organisms.csv', header=None)
orgs = list(orgs[0])

#------------------------------------------------------------------------------
# Always tell ncbi whom you are
Entrez.email = ""

# Create a short variable for esummary & record reading
read = Entrez.read
esummary = Entrez.esummary
esearch = Entrez.esearch

# Get a list of taxonomy ids
taxid_list = []
common_names = []

# Create a for loop to compile a list of taxonomy ids
for species in orgs:

    # Create a handle for the esearch
    taxid_search = esearch(db="taxonomy", term=species)
    pause(2)
    # Read and print the record or results of the search
    id_record = read(taxid_search)
    # Replace unwanted characters
    id_result = id_record['IdList']
    x = str(id_result)
    x = x.replace("'", "")
    x = x.replace("[", "")
    x = x.replace("]", "")

    # Append the id to the id list
    taxid_list.append(x)

    # Create a handle for the esummary
    name_search = esummary(db="taxonomy", id=x)
    pause(2)
    # Read and print the record or results of the search
    name_record = read(name_search)
    # Replace unwanted characters
    name_result = name_record[0]['CommonName']

    # Append the id to the id list
    common_names.append(name_result)

    # Keep updated on how this is progressing
    #print("Taxonomy ID: %s" % x, " | Species Name: %s" % species, " | Common Name: %s" % name_result)
print('Done.')