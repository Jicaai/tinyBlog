#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename:  allfile.py
# Author: Tiny
# Date:2011-03-26

import os
import fnmatch

def all_file(root, patterns='*'):
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
        for path in all_file(os.getcwd(),'*.pyc'):
                print path
