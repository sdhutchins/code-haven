# -*- coding: utf-8 -*-
"""
File Name:
Description: Use shutil to clone a directory.

Author: shutchins2
Date Created: Wed Apr  5 15:58:57 2017
Project Name:
"""
from shutil import copytree


def create_project_tree(destpath, name):
    project_name = name
    source = r'C:\\Users\\shutchins2\\Desktop\\GitRepo\\Example-Bioinformatics'
    destination = destpath + project_name
    copytree(source, destination)


destpath = r'C:\\Users\\shutchins2\\Desktop\\'
create_project_tree(destpath, 'Random')
