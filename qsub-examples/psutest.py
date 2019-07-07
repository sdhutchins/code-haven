# -*- coding: utf-8 -*-
import psutil
from subprocess import PIPE

cmd = ["python", "go.py"]
proc1 = psutil.Popen(cmd, stdout=PIPE)
print(proc1.pid)
proc1.wait()

cmd2 = ["python", "go2.py"]
proc2 = psutil.Popen(cmd2, stdout=PIPE)
print(proc2.pid)
