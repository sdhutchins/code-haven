# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 13:35:30 2016

@author: shutchins2
"""
### Use OpenMPI for multiprocessing or multithreading with parallel computing. ###

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("hello world from process ", rank)