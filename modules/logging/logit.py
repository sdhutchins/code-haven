# -*- coding: utf-8 -*-
"""
Date created: Sat Apr 22 20:45:17 2017
Author: S. Hutchins

Description: Main logging class

"""
import logging as log
import os
from datetime import datetime as d
import sys

#------------------------------------------------------------------------------
class Logit():
    def __init__(self, logfile, logname):

        # Variables for logging formats
        message_format = '%(name)s - [%(levelname)-2s]: %(message)s'


        if sys.platform == 'win32':
            logappend_format = '%m-%d-%Y_%I-%M-%p'
            pass
        elif sys.platform == 'linux':
            logappend_format = '%m-%d-%Y@%I:%M:%S-%p'
            pass

        # Would be a great idea to add a log directory setup if that directory
        # doesn't exist.

        log.basicConfig(level=log.DEBUG,
                        format=message_format,
                        filename="logs/" + logfile + "_%s.log" % str(d.now().strftime(logappend_format)))
        self.log = log.getLogger(logname)

    def scriptinfo(self):
        # Write basic information to the log
        date_format = '%a %b %d at %I:%M:%S %p %Y'  # Used to add as a date
        # Write basic information to the log
        self.log.info("------------------------------------------------------------------")
        self.log.info("The script name is %s" % os.path.basename(sys.argv[0]))
        self.log.info("The script began on %s" % str(d.now().strftime(date_format)))
        self.log.info("------------------------------------------------------------------")



