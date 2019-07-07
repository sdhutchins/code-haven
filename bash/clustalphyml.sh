#!/bin/bash
one=$(qsub scripts/clustal.pbs)
echo $one
two=$(qsub -W depend=afterok:$one scripts/phyml.pbs)
echo $two

# This script runs 2 pbs scripts in succession.