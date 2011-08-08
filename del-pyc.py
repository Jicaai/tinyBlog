#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename:  del_pyc.py
# Author: iLazy
# Date:2011-03-26

import os
import fnmatch
def del_pyc(root, patterns='*'):
        """del all the pyc file in the current work space
        """
        patterns = patterns.split(';')
        for path, subdir, files in os.walk(root):
                for name in files:
                        for pattern in patterns:
                               if fnmatch.fnmatch(name, pattern.strip()):
                                        yield os.path.join(path, name)

if __name__=='__main__':
        for path in del_pyc(os.getcwd(),'*.pyc; *.swp'):
                print path
                os.remove(path)

