# -*- coding: utf-8 -*-
"""
Last updated on November 16, 2016

@author: Shaurita D. Hutchins

"""
# I'm using this test to learn how read .csv or excel files with the pandas module as well as how to create excel files
# using pandas. Ultimately, I want to use pandas with the Bokeh module and to produce high level visualizations.

# List of modules used
import pandas as pd
import os

# Designate the directory of the file I'm using
home = r'C:\Users\shutchins2\Desktop'

# Change to the home directory
os.chdir(home)

########################################################################################################################
# Using Pandas to read existing .csv files


# Use the pandas module to read this .csv file
# df = pd.read_csv('MAF.csv')
# print(df)
# print(df.dtypes)


########################################################################################################################
# Using Pandas to create .csv files

# Create data
names = ['Rob', 'Rita', 'Xiao']
points = [10, 8, 9]

# Create a data set that is matching
LabDataSet = list(zip(names,points))

# Create the data frame and designate the column names
df = pd.DataFrame(data = LabDataSet, columns=['Names', 'Points'])
print(df)
df.to_csv('data1.csv',index=False,header=False)
df.to_csv('data2.csv',index=False,header=False)

