# -*- coding: utf-8 -*-

from path2json import json_to_lists, make_project_dir

path = r'C:\\Users\\shutchins2\\Desktop\\GitRepo\\KARG-Project'
outpath = r'C:\\Users\\shutchins2\\Desktop\\GitRepo\\'


top_dir_names = json_to_lists(path, 'kargproject')
make_project_dir(outpath, name='Test-Project', dirnames=top_dir_names)