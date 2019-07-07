# -*- coding: utf-8 -*-
import pandas as pd

initial = pd.read_csv('mal.csv')

postblast = pd.read_csv('maf.csv', error_bad_lines=False)
df1 = pd.DataFrame(postblast)
df1 = df1.dropna(how='all')

notfound = pd.read_csv('mal.csv', header=None)
nf = list(notfound[0])

col1 = list(initial.Tier)
col2 = list(initial.Gene)

gl = []
tl = []
for gene, c in zip(col2, col1):
    if gene in nf:
        print('Leave out %s' % gene)
        pass
    else:
        gl.append(gene)
        tl.append(c)
        len(gl)
        len(tl)

df2 = pd.DataFrame(tl, columns=['Tier'])
frames = [df2, df1]
last = pd.concat(frames, axis=1)
last.to_csv('Master_Accession_File.csv', index=False)
