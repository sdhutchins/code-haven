# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 16:29:52 2016

@author: Shaurita D. Hutchins
"""
# Part 3: Use multiple sequence alignments in phylip format to create phylogenetic trees.

# Mark start of program with printed text description/title.
print("\n" + (81 * "#") + "\n" + "#### Part 3:  Use multiple sequence alignments to create phylogenetic trees. ####" + "\n" + (81 * "#") + "\n")

# List of modules imported.
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import AlignIO

#alignment = AlignIO.read("HTR1E_aligned.phy", "phylip")
#print(alignment)
#print("\n")
#for record in alignment:
#    print(record.seq + " " + record.id + "\n")
#calculator = DistanceCalculator('identity')
#dm = calculator.get_distance(alignment)
#print(dm)

x = AlignIO.convert("HTR1E_aligned.fasta", "fasta", "HTR1E_aligned.phy", "phylip-relaxed")
print(x)
#tree = Phylo.read('outtree.txt', 'newick')
#tree.ladderize()   # Flip branches so deeper clades are displayed at top
#Phylo.draw(tree)

