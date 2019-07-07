# Author: SDH
# Date Created: Tue May 23 05:12:06 PM 2017
# Project Name: Psutil Test PID
# Description: do things

#PBS -S /bin/bash
#PBS -m bea
#PBS -M shutchins2@umc.edu
#PBS -l select=3:ncpus=1:mem=6gb -l place=free
#PBS -l cput=75:00:00
#PBS -l walltime=75:00:00
#PBS -N psutil
#PBS -o go.o${PBS_JOBID}
#PBS -e go.e${PBS_JOBID}
#PBS -j oe

cd ${PBS_O_WORKDIR}

python3 go.py

mail -s "script completed" shutchins2@umc.edu < "Fin."