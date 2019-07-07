from tkinter import *
from pandastable import Table
#assuming parent is the frame in which you want to place the table
pt = Table(parent)
pt.importCSV('example.csv')
pt.show()