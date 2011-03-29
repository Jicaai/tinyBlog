#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename:  del_pyc.py
# Author: iLazy
# Date:2011-03-26

import os
import fnmatch

def del_pyc(root, patterns='*'):
        """docstring for all_file""
        """
        patterns = patterns.split(';')
        for path, subdir, files in os.walk(root):
                for name in files:
#                        yield name
                        for pattern in patterns:
#                                yield pattern
                               if fnmatch.fnmatch(name, pattern.strip()):
                                        yield os.path.join(path, name)

if __name__=='__main__':
        for path in del_pyc(os.getcwd(),'*.pyc'):
                print path
                os.remove(path)
