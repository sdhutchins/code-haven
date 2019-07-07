# -*- coding: utf-8 -*-
"""
Date created: Thu Mar  2 15:32:35 2017
Author: S. Hutchins

Script description:

"""

import multiprocessing as mul
import os

def download(url):
    os.system('wget '+url)


dlist = ['www.163.com','www.qq.com','www.ifeng.com','www.baidu.com','www.sina.com.cn']

pool = mul.Pool(3)
pool.map(download, dlist)