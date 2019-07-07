# -*- coding: utf-8 -*-
"""
File Name: multiprocess_functions.py
Description:

Author: shutchins2
Date Created: Mon Apr  3 16:15:40 2017
Project Name: Orthologs Project
"""
# Modules used
import re
import os
import fnmatch
import logging as log
import pandas as pd
from datetime import datetime as d
from multiprocessing import Pool
from time import time
from OrthoTools import clustal_align, relaxphylip, ete3paml, SplitLists
import sys

#------------------------------------------------------------------------------
# Home Directory
home = os.getcwd() + '/' # Use templating for directory name
h = home
os.chdir(h)

#------------------------------------------------------------------------------
# Set up logging
log.basicConfig(filename="logs/clustal.log", level=log.INFO)
log.info("#------------------------------------------------------------------")
log.info("The script name is %s" % os.path.basename(__file__))
log.info("The date and time is currently %s" % str(d.now()))
log.info("#------------------------------------------------------------------")
log.info("Run clustal omega.")

# Create the main output directories if they don't exist
clustal_out = 'data/clustal-output/'
paml_out = 'data/paml-output/'
phyml_out = 'data/phyml-output/'

#------------------------------------------------------------------------------
dir_list = [clustal_out, phyml_out, paml_out]  # List of directories

for directory in dir_list:
    if os.path.exists(directory) == True:
        log.info('The directory %s exists.' % directory)
    else:
        os.mkdir(directory)
        log.info('The directory %s has been created' % directory)

#------------------------------------------------------------------------------
def genes2align():
    """ Get the list of genes based on pattern matching."""
    files = os.listdir('data/cds/')
    geneslist = []

    for filename in files:
        if fnmatch.fnmatch(filename, '*.ffn'):
            try:
                found = re.search('MASTER_(.+?)_CDS1.ffn', filename).group(1)
                geneslist.append(found)
            except AttributeError:
                log.error('There was an error in this attribute.')
        else:
            pass

    log.info("The genes are: %s " % geneslist)
    log.info("There are %s genes." % len(geneslist))

#------------------------------------------------------------------------------
    # Save the list of genes that will be aligned & analyzed via PAML to the
    # clustal output dir
    df = pd.DataFrame(geneslist)
    df.to_csv(clustal_out + 'genes_to_align.txt', sep='\t', index=False, header=None)

#------------------------------------------------------------------------------
    # Check to see if any alignment directories exist
    aligned = []
    for gene in geneslist:
        os.chdir(clustal_out)
        path = gene + "_Aligned/"
        if os.path.exists(path) == True:
            log.info("%s directory exists." % path)
            os.chdir(path)
            file = gene + "_aligned.phy"
            if os.path.exists(file) == True:
                log.info("%s exists." % file)
                aligned.append(gene)
                log.info("%s was removed from the list." % gene)
                os.chdir(h)
            else:
                os.chdir(h + clustal_out)
                os.system("rm -R " + path + " -f")
                log.info("The %s directory was deleted." % path)
                os.chdir(h)
        else:
            os.chdir(h)
            pass

    log.info("The aligned genes are: %s " % aligned)
    log.info("There are %s aligned genes." % len(aligned))

    # Create a new list of unaligned genes
    finalgeneslist = []
    for g in geneslist:
        if g not in aligned:
            finalgeneslist.append(g)

    log.info("The unaligned genes are: %s " % finalgeneslist)
    log.info("There are %s unaligned genes." % len(finalgeneslist))

    listgroups = SplitLists(finalgeneslist, 'genes', n=int(40))
    return listgroups
#------------------------------------------------------------------------------
# Definitions that incorporate clustal and paml with multiprocessing.
def clustal(gene):
    """Input a file of sequences to clustal omega in order to get a multiple
    sequnce alignment that will be analyzed for species divergence per gene with
    PAML."""
    # Create clustal omega gene directories
    gene_aligned_dir = clustal_out + gene + '_Aligned/'
    os.mkdir(gene_aligned_dir)

    # Copy file of sequences to output directory
    os.system('cp data/cds/MASTER_' + gene + '_CDS1.ffn ' + gene_aligned_dir)
    os.chdir(gene_aligned_dir)

    # Run clustal omega
    clustal_align(gene)
    log.info('Clustal omega has created a multiple sequence alignment for %s' % gene)

    # Run relaxphylip definition
    relaxphylip(gene)

    # Change to home directory
    os.chdir(h)

#    # Create phyml gene directories
#    gene_phyml_dir = phyml_out + gene + '_PhyML/'
#    if os.path.exists(gene_phyml_dir) == True:
#        os.chdir(gene_phyml_dir)
#        phyfile = gene + '_aligned.phy '
#        if os.path.exists(phyfile) == True:
#            pass
#        else:
#            os.chdir(h)
#            os.system('cp ' + gene_aligned_dir + gene + '_aligned.phy ' + gene_phyml_dir)
#    else:
#        os.mkdir(gene_phyml_dir)
#        os.system('cp ' + gene_aligned_dir + gene + '_aligned.phy ' + gene_phyml_dir)
#        os.chdir(h)
#------------------------------------------------------------------------------
def paml(gene):
    """Input a phylip formated multiple sequence alignment to PAML in order to
    analyze divergence using the."""
    # Create paml gene directories
    gene_aligned_dir = clustal_out + gene + '_Aligned/'
    gene_paml_dir = paml_out + gene + '_PAML/'
    os.mkdir(gene_paml_dir)

    # Copy phylip file to directory
    os.system('cp ' + gene_aligned_dir + gene + '_aligned.phy ' + gene_paml_dir)
    os.chdir(gene_aligned_dir)

    # Run clustal omega
    ete3paml(gene)
    log.info('PAML has created output for %s' % gene)

    # Change to home directory
    os.chdir(h)

#------------------------------------------------------------------------------
def main(function, geneslist):
    """This function uses a pool to start multiple processes to get clustal and
    PAML output. The argument (geneslist) should be a list of genes.
    """
    if len(geneslist) > 0:
        print(geneslist)
        ts = time()
        with Pool(processes=4) as p:
            p.map(function, geneslist)
            log.info("Multiprocessing with 8 processes has begun.")
            log.info("It took {} hours to get all algnments.".format((time() - ts)/3600))
    elif len(geneslist) == 0:
        sys.exit("There are no genes that need to be aligned in your genes list.")

#------------------------------------------------------------------------------
