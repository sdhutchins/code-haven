import os
import random
import string
import tempfile
import subprocess


def random_id(length=8):
    return ''.join(random.sample(string.ascii_letters + string.digits, length))

TEMPLATE_SERIAL = """
#$ -S /bin/bash
#$ -cwd
#$ -N {job_name}
#$ -e {errfile}
#$ -o {logfile}
#$ -pe make {slots}

echo "------------------------------------------------------------------------"
echo "Job started on" `date`
echo "------------------------------------------------------------------------"
{script}
mail -s "{script_name}.py script completed" shutchins2@umc.edu < logs/{script_name}.log
"""

def submit_python_code(code, name="job", logfile="output.$JOB_ID", errfile="error.$JOB_ID", cleanup=True, prefix="", slots=1):
    base = prefix + "submit_{0}".format(random_id())
    open(base + '.py', 'w').write(code)
    script = "python3 " + base + ".py"
    open(base + '.pbs', 'w').write(TEMPLATE_SERIAL.format(script=script, script_name=base, job_name=name, logfile=logfile, errfile=errfile, slots=slots))
    try:
        #subprocess.call('qsub  ' + base + '.pbs', shell=True)
        print(base)
    finally:
        if cleanup:
            print(base)
            #os.remove(base + '.qsub')

submit_python_code(code="")