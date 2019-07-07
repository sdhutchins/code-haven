# -*- coding: utf-8 -*-
"""
Date created: Mon Feb 20 15:51:50 2017
Author: S. Hutchins

Script description: This script will import a .xls file (as a result of Victor
plate read) and turn it into a csv that is ready for use with graphpad prism.

"""
# Modules used
import pandas as pd
from pandas import ExcelWriter

#------------------------------------------------------------------------------

# Import xls file
# Select the sheet that has your data
file = pd.read_excel('d46.xls', sheetname='Plate_Page1')

# Select the rows that have data in them by printing the file to see
data = file[5:8] # Data should start at row 5 for every victor file

# Create a dataframe for the data
df = pd.DataFrame(data=data, dtype=str)

# Rename the columns
d4project = {"Plate": "-4", "Repeat": "-5", "End time": "-6", "Start temp.": "-7",
          "End temp.": "-8", "BarCode": "-9", "Unnamed: 6": "-10", "Unnamed: 7": "-11",
          "Unnamed: 8": "-12", "Unnamed: 9": "10 uM D4 agonist", "Unnamed: 10": "100 uM Forskolin",
          " ": "Control"}

df = df.rename(columns=d4project)
df2 = df.T  # Transpose the dataframe for this project

# Save the cleaned up data as a xls file
writer = ExcelWriter('d4#6.xlsx')  # Use the ExcelWriter and name the file
df.to_excel(writer, sheet_name='D4.4 Data Feb 17, 2017', index=False, float_format=str)
df2.to_excel(writer, sheet_name='Transposed', header=False)
writer.save()  # Save the file