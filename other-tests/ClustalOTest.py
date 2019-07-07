# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:49:49 2016

@author: shutchins2
"""
# List of modules used
from Bio.Align.Applications import ClustalOmegaCommandline

# Output in phylip format
print("\n" + "Clustal Ω will align the sequences and produce output in phylip format." + "\n")
in_file1 = "GABBR2_cds.fasta"
out_file1 = "GABBR2_aligned.phy"
clustalo_cline1 = ClustalOmegaCommandline(infile=in_file1, outfile=out_file1, seqtype="DNA",
                                          infmt="fasta", outfmt="phylip", iterations=4, distmat_full_iter=True, verbose=True, force=True)
#stdout1, stderr1 = clustalo_cline1()
#clustalo_cline1()
print(clustalo_cline1)  # Prints the command line text
#print(stdout1, stderr1)
#print("Phylip formatted alignment file has been created." + "\n")   