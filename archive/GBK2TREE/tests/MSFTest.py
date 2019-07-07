# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 10:46:25 2016

@author: shutchins2
"""

#Part 2: Align multiple sequences located in fasta files using Clustal Omega via MCSR and create .fasta, .aln, and .phylip output formats.

# List of modules used
import os
import sys
from Bio.Align.Applications import ClustalOmegaCommandline

# Mark start of program with printed text.
print("\n" + (70 * "#") + "\n" + "#### Part 2:  Align fasta files using Clustal Omega via the MCSR. ####" + "\n" + (70 * "#") + "\n")

os.system("set -x")
os.system("cat *_cds.fasta* > HTR1A_cds.fasta") # Use command line to concatenate fasta files in current directory

#input("If you would like to create a fasta file, press ENTER. ")   
## Output in fasta format
print("\n" + "Lastly, clustal Ω will align the sequences and produce output in msf format." + "\n")
in_file = "HTR1A_cds.fasta"
out_file = "HTR1A_cds_aligned.msf"
clustalo_cline = ClustalOmegaCommandline(profile1="HTR1A_Homo_sapiens_cds.fasta", profile2="HTR1A_Macaca_mulatta_cds.fasta", infile=in_file, outfile=out_file, seqtype="DNA", 
                                         infmt="fasta", outfmt="msf", distmat_full_iter=True, iterations=2, verbose=True, 
                                         threads=8, log="HTR1A_msf_log.txt", force=True)
stdout, stderr = clustalo_cline()                                         
clustalo_cline()
print(stdout, stderr)   
print("MSF formatted alignment file has been created." + "\n")


sys.exit("✓✓✓✓ This script has completed. ✓✓✓✓")