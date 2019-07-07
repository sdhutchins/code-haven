# -*- coding: utf-8 -*-
"""
Last updated on November 21, 2016

@author: Shaurita D. Hutchins

"""

# I'm learning how to use the input function with if to generate a file with the proper data that I want.
# I'll be integrating this with unix

# List of modules
import os

# Describe the input variables

a = input("What is your name? ")
b = "James"
c = "Mike"

if a==b or a==c:
    print("I love you, " + a)
else:
    print("I don't know you!")
