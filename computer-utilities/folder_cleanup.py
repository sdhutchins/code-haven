# -*- coding: utf-8 -*-
"""
Date created: Thu Mar  9 17:11:18 2017
Author: S. Hutchins

Script description: Cleanup downloads folder.

* Incorporate logging into this script and schedule it.

"""
# Modules Used
import os
import pathlib
import logging as log
from datetime import datetime as d
from shutil import rmtree, move
import zipfile

#------------------------------------------------------------------------------
# Set up the logger
format1 = '%a %b %d %I:%M:%S %p %Y'  # Used to add as a date
format2 = '%m-%d-%Y_%I-%M-%S-%p'  # Used to append to archives

log.basicConfig(filename="logs\directory_archiving.log", level=log.INFO)
log.info("#------------------------------------------------------------------")
log.info("The script name is %s" % os.path.basename(__file__))
log.info("The date and time is currently %s" % str(d.now().strftime(format1)))
log.info("#------------------------------------------------------------------")

#------------------------------------------------------------------------------
# Use paths
downloads = r'C:\Users\shutchins2\Downloads'

os.chdir(downloads)

filetypes = []
for file in os.listdir():
    ext = pathlib.PureWindowsPath(file).suffix or pathlib.PurePosixPath(file).suffix
    if ext == '':
        log.info(file + " does not end in an extension.")
        pass
    elif ext == '.ini':  # This is a file that windows creates
        pass
    else:
        extname = ext.replace(".", "")
        filetypes.append(extname)

        for ft in filetypes:
            root_path = downloads
            folder = ft + '_downloads'
            # If the filetype folder exists, move files of that type to it
            if os.path.isdir(folder) == True:
                log.info("The %s directory exists." % folder)
                os.system('move *.' + ft + ' ' + folder)
                log.info("The file, %s, was moved to the %s directory." % (file, folder))
            else:
                # If the filetype folder does not exist, create it and
                # move files of that type to it
                os.mkdir(folder)
                log.info("The %s directory exists." % folder)
                os.system('move *.' + ft + ' ' + folder)
                log.info("The file, %s, was moved to the %s directory." % (file, folder))

# After doing moving files to each file type directory, create an
# archive with all directories in it & zip it.
directories = os.listdir()
arch = 'downloads_archive_%s' % str(d.now().strftime(format2))

# Move all of the directories to an folder
for directory in directories:
    move(directory, arch)

# Create the zip file.
dloadzip = zipfile.ZipFile(arch + '.zip', 'w', zipfile.ZIP_DEFLATED)

# Use os.walk to write all files and subdirectories to the zip file
for base, dirs, files in os.walk(arch):
    for f in files:
        dloadzip.write(os.path.join(base, f), os.path.join(base, f))

dloadzip.close()  # Close the zip file!!!!
rmtree(arch)  # Remove the non-zipped archive directory

log.info("The zip file (%s) has been created and saved." % dloadzip)
log.info("This script is complete.")
log.shutdown()



