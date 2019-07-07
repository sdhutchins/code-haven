# -*- coding: utf-8 -*-
import re

from tabula import read_pdf

df = read_pdf("canton_naacp_roster.pdf", pages="all",
              pandas_options={'header': None})

#df.to_csv('canton_msnaacp_roster.csv', index=False)

names = []
numbers = []

for index, row in df.iterrows():
    if bool(re.search(r'\d', str(row[0]))) is False:
        regex = re.compile("([A-Z]{1}[a-z]+) ([A-Z]{1}[a-z]+)$")
        if regex.search(str(row[0])) is not None:
            # TODO: Figure out how to print this without parentheses
            print(regex.findall(str(row[0]))[0])
