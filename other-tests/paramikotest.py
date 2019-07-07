# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 12:46:29 2016

@author: shutchins2
"""

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='hpcwoods.olemiss.edu', username='r2295', password='')
status =  ssh.get_transport().is_active() #returns True if connection is alive/active
stdin, stdout, stderr = ssh.exec_command('less human.txt')
print(stdout.read())
