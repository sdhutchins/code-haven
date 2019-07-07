# -*- coding: utf-8 -*-
"""
File Name:
Description: This script creates a shell directory structure similar to the path
inserted into the script.

Author: shutchins2
Date Created: Wed Apr  5 14:20:49 2017
Project Name:
"""
import os
import json


def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path, x)) for x in os.listdir(path) if x != '.git']
    else:
        d['type'] = "file"
    return d


def save_to_json(path, jsonfilename):
    data = path_to_dict(path)
    with open(jsonfilename + '.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)


def json_to_project(jsonfile):
    with open(jsonfile, 'r') as f:
        dirdict = json.load(f)

    return dirdict


def write_file(filename):
    file = open(filename, "w")
    file.close()

pathdict = json_to_project('example.json')

rootdir = pathdict['name']
os.makedirs(rootdir, exist_ok=True)
for key in pathdict['children']:
    if key['type'] == 'directory':
        topdir = os.path.join(rootdir, key['name'])
        os.makedirs(topdir, exist_ok=True)
        for key in key['children']:
            if key['type'] == 'directory':
                subdir = os.path.join(topdir, key['name'])
                os.makedirs(subdir, exist_ok=True)
            elif key['type'] == 'file':
                write_file(os.path.join(topdir, key['name']))
    elif key['type'] == 'file':
        write_file(os.path.join(rootdir, key['name']))
