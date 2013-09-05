#!/usr/bin/env python
"""
merge two files with 2 columns base on keys in 1st column 
"""
__version__ = '0.1'
__author__ = 'jmadzo'

import sys
import argparse

if len(sys.argv)==1: sys.exit("missing arguments\nfor help --help or -h")

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-a',action='store', dest='file_a', help='input smaller file a')
parser.add_argument('-b',action='store', dest='file_b', help='input bigger file b')
command_line=parser.parse_args()
file_a=command_line.file_a
file_b=command_line.file_b

with open(file_a, 'rU') as file_a:
    a=dict(line.strip().split("\t",1) for line in file_a)

with open(file_b, 'rU') as file_b:
    for row in file_b:
        key_b, value_b=row.strip().split("\t",1)
        try:
            if key_b in a: #.keys(): 
                print key_b+"\t"+a[key_b]+"\t"+value_b
                del a[key_b]
            else: 
                print key_b+"\t-\t-\t-\t"+value_b
        except Exception as err:
            raise err
            pass
for key_a in a: print key_a+"\t"+a[key_a]+"\t-\t-\t-" 
        