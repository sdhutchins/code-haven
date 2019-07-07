# -*- coding: utf-8 -*-
"""
File Name:
Description:

Author: Shaurita Hutchins
Date Created: Fri Mar 31 14:13:39 2017
Project Name:
"""
import os

# Create directories

def create_subdirs(subdirname):
    """Quick utility that uses the home directory as the base directory.
    This allows users to input a subdirectory such as '/data/blast/blast-xml'.
    If none of those directories exist, they'll be created.'

    This is for use on a linux or unix system."""
    home = os.getcwd()
    subdirname = home + subdirname
    os.makedirs('%s' % subdirname, exist_ok=True)  # Create the directory
    return print("%s directory created" % subdirname);

create_subdirs(r'\this\will\be\fun')