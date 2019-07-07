# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 14:40:55 2016

@author: shutchins2
"""
# This script is designed to create a gi list for each taxonomy id based on
# the refseq_rna database on the MCSR & use threading.

# List of modules used
import threading
from queue import Queue
import time
import sys
import os
import csv

# Mark start of program with printed text.
print("\n" + (105 * "#") + "\n" + "Create a GI list for each organism using the \
taxonomy id and the command, blastdbcmd, on the MCSR.  ####" + "\n" + (105 * "#") + "\n")

# lock to serialize console output
lock = threading.Lock()

def do_work(item):
    # Open taxids.csv which is a comma delimited list of all tax id's to be used.
    taxid = open('taxids.csv')  # 1st column - tax id's
    file1 = csv.reader(taxid)
    TaxID_count = 0


# Main "for" loop in this file that creates taxidgi.txt files in the home directory.
    for ID in file1:
        TaxID_count = TaxID_count + 1

        a = '/home/ums/r2295/bin/Orthologs-Project/'  # Home Directory
        home = a  # Location of taxids.csv
        os.chdir(home)  # Directory Change: Output directory

        # List of human accession numbers to be used.
        #acc_list = 8795, 45

        try:
            open(str(ID[0]) + "gi.txt", "w")
            os.system("blastdbcmd -db refseq_rna -entry all -outfmt '%g %T' | awk ' { if ($2 == " + str(ID[0]) + ") { print $1 } } ' >> " + str(ID[0]) + "gi.txt")
            print(str(ID[0]) + "gi.txt" + " has been created.")
        except FileExistsError:
            print(str(ID[0]) + "gi.txt" + "already exists.")
    time.sleep(.5) # pretend to do some lengthy work.

    # Make sure the whole print completes or threads can mix up output in one line.
    with lock:
        print(threading.current_thread().name,item)

# The worker thread pulls an item from the queue and processes it
def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()

# Create the queue and thread pool.
q = Queue()
for i in range(1):
     t = threading.Thread(target=worker)
     t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
     t.start()

# stuff work items on the queue (in this case, just a number).
start = time.perf_counter()
for item in range(4):
    q.put(item)

q.join()       # block until all tasks are done

sys.exit("The script has completed! ✓")