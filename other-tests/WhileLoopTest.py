# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 12:11:56 2016

@author: shutchins2
"""
import csv
t = open('taxids.csv')
file1 = csv.reader(t)

for ID in file1:
#    print(ID[0])
    ID = str(ID)
    print(str(ID))
