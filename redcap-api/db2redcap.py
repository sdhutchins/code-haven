# -*- coding: utf-8 -*-
"""
Date created: Tue Mar 21 18:06:42 2017
Author: S. Hutchins

Script description: Import a sqlite db into redcap.

* I'm sure this can be accessed via BioSQL

http://www.datacarpentry.org/python-ecology-lesson/08-working-with-sql/
"""
# Modules Used
import sqlite3
import pandas as pd
#from BioSQL import BioSeqDatabase

# Import or connect the the sql database
con = sqlite3.connect("Tier_1.db")

# Get a list of the tables from the database
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", con)
df = pd.DataFrame(tables)
tablelist = df['name'].tolist()

# From here, figure out a way to load each table to a dataframe.
# Then upload each dataframe to redcap.
# I need to research this more to figure out how the tables are configured.
# Each table/dataframe likely needs to be a record type.

cur = con.cursor()
for row in cur.execute('SELECT * FROM taxon;'):
    print(row)

# Be sure to close the connection
con.close()
