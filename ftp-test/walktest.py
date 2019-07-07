# -*- coding: utf-8 -*-
from ftplib import FTP, error_perm
import os
import pathlib
import json

ncbi = 'ftp.ncbi.nlm.nih.gov/'
refseqrna = '/blast/db/'  # Connect to this blastdb
blast = '/blast/'

class FtpWalker(object):
    def __init__(self, root='/', pwd):
        ftp = FTP("ftp.ncbi.nlm.nih.gov", timeout=None)
        self.ftp = ftp
        connection = self.ftp.login(user='anonymous', passwd=pwd)
        self.connection = connection
        self.root = root

    def listdir(self, _path=''):
        file_list, dirs, nondirs, extensions = [], [], [], []
        try:
            self.connection.cwd(_path)
        except Exception as exp:
            return [], []
        else:
            self.connection.retrlines('LIST', lambda x: file_list.append(x.split()))
            for info in file_list:
                ls_type, name = info[0], info[-1]
                if ls_type.startswith('d'):
                    dirs.append(name)
                else:
                    nondirs.append(name)  # These are files
                    for i in info:  # Use a for loop to get a list of extensions
                        # Get the filename suffix
                        ext = pathlib.PurePosixPath(i).suffix  # Get the filename suffix
                        #extname = ext.replace(".", "")
                        if ext not in extensions:  # Only add unique extensions
                            extensions.append(ext)

            return dirs, nondirs, extensions

    def walk(self, top, path=''):
        dirs, nondirs = self.listdir(top)
        yield (path or top), dirs, nondirs
        path = top
        for name in dirs:
            path = os.path.join(path, name)
            for x in self.walk(name, path):
                yield x
            self.connection.cwd('..')
            path = os.path.dirname(path)

    def to_json(self, top, path=''):
        dirs, nondirs = self.listdir(top)
        yield (path or top), dirs, nondirs
        path = top
        ftpdict = {}
        ftpdict = {'name': path}
        if os.path.isdir(path):
            ftpdict['type'] = "directory"
            ftpdict['children'] = [self.to_json(os.path.join(path, d)) for dirs in self.listdir(path) for d in dirs]
        else:
            ftpdict['type'] = "file"
        return ftpdict

        with open('ftp.json', 'w') as outfile:
            json.dump(ftpdict, outfile, indent=4)

ftp = FtpWalker(pwd="")