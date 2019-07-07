# -*- coding: utf-8 -*-
import tempfile

with tempfile.TemporaryFile() as fp:
    fp.write(b'Hello world!')
    fp.seek(0)
    fp.read()


with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)
