from ftplib import FTP
import os
import json

ncbi = 'ftp.ncbi.nlm.nih.gov'
refseqrna = '/blast/db/'  # Connect to this blastdb
blast = '/blast/'

def ftp_connect():
    """Connects to the FTP server and returns and instance of the connection.
    """
    ftp = FTP("ftp.ncbi.nlm.nih.gov", timeout=None)
    ftp.login(user='anonymous', passwd="")
    return ftp

def ftp_walk(target_dir=''):
    ftp = ftp_connect()
    file_list, dirs, nondirs = [], [], []
    try:
        ftp.cwd(target_dir)
    except Exception as exp:
        print("Current path: ", ftp.pwd(), exp.__str__(), target_dir)
        return [], []
    else:
        ftp.retrlines('LIST', lambda x: file_list.append(x.split()))
        for info in file_list:
            ls_type, name = info[0], info[-1]
            if ls_type.startswith('d'):
                dirs.append(name)
            else:
                nondirs.append(name)
        return dirs, nondirs

def to_json(self, path):
    ftpdict = {}
    ftpdict = {'name': path}
    if os.path.isdir(path):
        ftpdict['type'] = "directory"
        ftpdict['children'] = [self.to_json(os.path.join(path, d)) for dirs in self.listdir(path) for d in dirs]
    else:
        ftpdict['type'] = "file"
    #return ftpdict

    with open('ftp.json', 'w') as outfile:
        json.dump(ftpdict, outfile, indent=4)

