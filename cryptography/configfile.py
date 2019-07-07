# -*- coding: utf-8 -*-
"""
File Name:
Description:

Author: shutchins2
Date Created: Wed Apr 19 12:21:22 2017
Project Name:
"""

import configparser

config = configparser.ConfigParser()

# Add APIKEYS section
config['APIKEYS'] = {'slack': ''}

# Add Usernames section
config['USERNAMES'] = {'sdh': 'shutchins2', 'rag': 'rgilmore'}

# Add Servers section
config['SERVERS'] = {'digitalocean': ''}

# Writing our configuration file to 'example.cfg'
with open('orthologs.ini', 'w') as configfile:
    config.write(configfile)