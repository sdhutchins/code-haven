# -*- coding: utf-8 -*-
"""
This program will open a ssh terminal and login to MCSR.

Created on Thu Sep  1 15:40:33 2016

Author: Shaurita D. Hutchins
"""
import paramiko
 
def runSshCmd(hostname, username, password, cmd, timeout=None):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password,
            allow_agent=False, look_for_keys=False, timeout=timeout)
 
    stdin, stdout, stderr = client.exec_command(cmd)
    data = stdout.read()
    return data

pwd = ""
runSshCmd(hostname="hpcwoods.olemiss.edu", username="r2295", password=pwd, "ls -h")
