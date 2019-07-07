# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:44:03 2016

@author: Shaurita D. Hutchins
"""
# Part 2: Align multiple sequences located in fasta files using Clustal Omega
# via MCSR and create .fasta, .aln, and .phylip output formats.

# List of modules used
import os
import sys
from Bio.Align.Applications import ClustalOmegaCommandline

# Mark start of program with printed text.
print("\n" + (70 * "#") + "\n" + "#### Part 2: Align fasta files using Clustal Omega via the MCSR.  ####" + "\n" + (70 * "#") + "\n")

# Echos all commands in the current shell.
os.system("set -x")

# Creates a temporary directory for the profile sequence/hmm and move it to that directory.
os.system("mkdir temp | mv HTR1A_Homo_sapiens_cds.fasta temp")

# Uses command line to concatenate fasta files in current directory.
os.system("cat *_cds.fasta* > HTR1A_cds.fasta")

#############################################################################################################
# Create definitions or not?

#def clustalo_clustal():
#    in_file = str(Gene[0]) + "_cds.fasta"
#    out_file = str(Gene[0]) + "_cds_aligned.aln"
#    clustalomega_cline = ClustalOmegaCommandline(infile=in_file, outfile=out_file, verbose=True, auto=True)
#    print(clustalomega_cline)
#    clustalomega_cline()

#def clustalo_fasta():
#    in_file = str(Gene[0]) + "_cds.fasta"
#    out_file = str(Gene[0]) + "_cds_aligned.fasta"
#    clustalomega_cline2 = ClustalOmegaCommandline(infile=in_file, outfile=out_file, verbose=True, auto=True)
#    print(clustalomega_cline2)
#    clustalomega_cline2()

#def clustalo_phylip():
#    in_file = str(Gene[0]) + "_cds.fasta"
#    out_file = str(Gene[0]) + "_cds_aligned.phylip"
#    clustalomega_cline3 = ClustalOmegaCommandline(infile=in_file, outfile=out_file, verbose=True, auto=True)
#    print(clustalomega_cline3)
#    clustalomega_cline3()
#############################################################################################################

print("\n")

# Output in clustal format
# input("If you would like to align sequences and create clustal, phylip, fasta, and msf files as output, press ENTER. ")
print("\n" + "Firstly, clustal Ω will align the sequences and produce output in clustal format." + "\n")
in_file = "HTR1A_cds.fasta"
out_file = "HTR1A_cds_aligned.aln"
clustalo_cline1 = ClustalOmegaCommandline(profile1="/temp/HTR1A_Homo_sapiens_cds.fasta",infile=in_file, outfile=out_file, seqtype="DNA", 
                                         infmt="fasta", outfmt="clustal", iterations=2, distmat_full_iter=True, verbose=True, 
                                         threads=8, force=True, log="HTR1A_aln_log.txt")
stdout1, stderr1 = clustalo_cline1()                                         
clustalo_cline1()
print(stdout1, stderr1)
print("\n" + "Clustal formatted alignment file has been created." + "\n")


# input("If you would like to create a phylip file, press ENTER. ")
# Output in phylip format
print("\n" + "Secondly, clustal Ω will align the sequences and produce output in phylip format." + "\n")
in_file2 = "HTR1A_cds.fasta"
out_file2 = "HTR1A_cds_aligned.phy"
clustalo_cline2 = ClustalOmegaCommandline(profile1="/temp/HTR1A_Homo_sapiens_cds.fasta", infile=in_file2, outfile=out_file2, seqtype="DNA", 
                                         infmt="fasta", outfmt="phylip", iterations=2, distmat_full_iter=True, verbose=True, 
                                         threads=8, force=True, log="HTR1A_phy_log.txt")
stdout2, stderr2 = clustalo_cline2()
clustalo_cline2()
print(stdout2, stderr2)
print("Phylip formatted alignment file has been created." + "\n")


# input("If you would like to create a fasta file, press ENTER. ")
# Output in fasta format
print("\n" + "Thirdly, clustal Ω will align the sequences and produce output in fasta format." + "\n")
in_file3 = "HTR1A_cds.fasta"
out_file3 = "HTR1A_cds_aligned.fasta"
clustalo_cline3 = ClustalOmegaCommandline(profile1="/temp/HTR1A_Homo_sapiens_cds.fasta", infile=in_file3, outfile=out_file3, seqtype="DNA", 
                                         infmt="fasta", outfmt="fasta", iterations=2, distmat_full_iter=True, verbose=True, 
                                         threads=8, force=True, log="HTR1A_fasta_log.txt")
stdout3, stderr3 = clustalo_cline3()                                         
clustalo_cline3()
print(stdout3, stderr3)
print("Fasta formatted alignment file has been created." + "\n")


# input("If you would like to create a msf file, press ENTER. ")
# Output in msf format
print("\n" + "Lastly, clustal Ω will align the sequences and produce output in msf format." + "\n")
in_file4 = "HTR1A_cds.fasta"
out_file4 = "HTR1A_cds_aligned.msf"
clustalo_cline4 = ClustalOmegaCommandline(profile1="/temp/HTR1A_Homo_sapiens_cds.fasta",
                                          infile=in_file4, outfile=out_file4, seqtype="DNA",
                                          infmt="fasta", outfmt="msf",
                                          distmat_full_iter=True, iterations=2,
                                          verbose=True,
                                          threads=8, log="HTR1A_msf_log.txt",
                                          force=True)
stdout4, stderr4 = clustalo_cline4()
clustalo_cline4()
print(stdout4, stderr4)
print("MSF formatted alignment file has been created." + "\n")


sys.exit("✓✓✓✓ This script has completed. ✓✓✓✓")
