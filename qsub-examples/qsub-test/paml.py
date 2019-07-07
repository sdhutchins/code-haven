# -*- coding: utf-8 -*-
"""
File Name: test.py
Description: The purpose of this tool is to integrate qsub functions, multprocessing, and
phylogenetics in order to create multiple jobs.

Author: S. Hutchins
Date Created: Wed May  3 13:26:43 2017
Project Name: Orthologs Project
"""

# Modules used
from QsubTools import SubmitPythonCode, ImportTemp
from multiprocess_functions import genes2align

#------------------------------------------------------------------------------
# Import the pbs and script templates
pbs_temp = ImportTemp(filepath='templates/temp.pbs')

script_temp = """from multiprocess_functions import main, clustal
main(geneslist={}, function=paml)
    """

list_chunks = genes2align()

for k, v in list_chunks.items():
    # Format the script template with the list of genes to align or run PAML on
    # Submit the python code and create qsub jobs
    SubmitPythonCode(code=script_temp.format(v), pbstemp=pbs_temp, author="SDH", jobname="karg-paml")

# The next major part to add is creation of a bash script or waiting for
# the genes to align in order to start paml