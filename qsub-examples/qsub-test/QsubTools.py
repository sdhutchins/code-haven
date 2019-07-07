# -*- coding: utf-8 -*-
# Modules Used
import os
import random
import string
#import tempfile
import subprocess
from string import Template
from datetime import datetime as d
import psutil

#------------------------------------------------------------------------------
def ImportTemp(filepath):
    """Import the script or file that you need a template of and that has temp
    strings."""
    file_temp = open(filepath, 'r')
    file_str = file_temp.read()
    file_temp.close()

    file_temp = Template(file_str)
    return file_temp

#------------------------------------------------------------------------------
def File2Str(filename):
    file_temp = open(filename, 'r')
    file_str = file_temp.read()
    return file_str

#------------------------------------------------------------------------------
def pbs_dict(author, description, project, select, jobname, script, logname, cmd,
             gb='6gb', cput='75:00:00', walltime='75:00:00'):
    # Date format
    format1 = '%a %b %d %I:%M:%S %p %Y'  # Used to add as a date

    pbs_dict = {
        'author': author,
        'description': description,
        'date': d.now().strftime(format1),
        'PBS_JOBID': '${PBS_JOBID}',
        'PBS_O_WORKDIR': '${PBS_O_WORKDIR}',
        'proj_name': 'Orthologs Project',
        'select': int(select),
        'memgb': gb,
        'cput': cput,
        'wt': walltime,
        'job_name': jobname,
        'script': script,
        'log_name': logname,
        'cmd': script
        }

    return pbs_dict

#------------------------------------------------------------------------------
def RandomId(length=5):
    return ''.join(random.sample(string.ascii_letters + string.digits, length))

#------------------------------------------------------------------------------
def SubmitPythonCode(code, pbstemp, author, jobname="job", cleanup=True, prefix="", slots=1):
    """ This function creates and submits qsub jobs."""

    format1 = '%a %b %d %I:%M:%S %p %Y'  # Used to add as a date

    # Create a base name for the jobs and python scripts
    base = prefix + "submit_{0}".format(RandomId())

    with open('tempfiles/' + base + '.py', 'w') as pyfile:
        pyfile.write(code)
        pyfile.close()

    script = "/home1/ums/r2295/.conda/envs/ete3/bin/python tempfiles/" + base + ".py"

    pbs_dict = {
            'author': author,
            'description': 'do things',
            'date': d.now().strftime(format1),
            'PBS_JOBID': '${PBS_JOBID}',
            'PBS_O_WORKDIR': '${PBS_O_WORKDIR}',
            'proj_name': 'Orthologs Project',
            'select': '3',
            'memgb': '6gb',
            'cput': '75:00:00',
            'wt': '75:00:00',
            'job_name': jobname,
            'script': script,
            'log_name': base,
            'cmd': script
            }

    with open('tempfiles/' + base + '.pbs', 'w') as pbsfile:
        pbsfile.write(pbstemp.substitute(pbs_dict))
        pbsfile.close()

#    try:
#        cmd = 'qsub  tempfiles/' + base + '.pbs'
#        cmd_status = subprocess.call([cmd], shell=True)
#        if cmd_status == 0:  # Command was successful.
#            print("Job submitted.")
#            pass  # Continue through script.
#        else:  # Unsuccessful. Stdout will be '1'.
#            print("PBS job not submitted.")
#    finally:
#        if cleanup:
#            pass
##            os.remove(base + '.qsub')
##            os.remove(base + '.py')

    try:
        cmd = 'qsub tempfiles/' + base + '.pbs'
        process = psutil.Popen([cmd], shell=True)
        if process == 0:  # Command was successful.
            print(process.pid)
            print("Job submitted.")
            pass  # Continue through script.
        else:  # Unsuccessful. Stdout will be '1'.
            print("PBS job not submitted.")
    finally:
        if cleanup:
            pass
#            os.remove(base + '.qsub')
#            os.remove(base + '.py')

#------------------------------------------------------------------------------

