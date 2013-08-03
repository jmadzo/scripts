#!/usr/bin/env python
"""
counts numbers of bp in overlap,  bedtools intersect
bed file entries are merged before and after intersection in order to avoid to count same bp multiple times
"""

from __future__ import division
__version__ = '1.0'
__author__ = 'jmadzo'

import sys
import argparse
import pybedtools

def main():
	'''main function'''
	###################### check arguments ############################################
	if len(sys.argv)==1: sys.exit('\n no arguments provided, for help: --help')
	##############################  parsing arguments  ################################
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument('-a', action='store', dest='file_A', help='input file A')
	parser.add_argument('-b', action='store', dest='file_B', help='input file B')
	
	command_line=parser.parse_args()
	fileA=command_line.file_A
	fileB=command_line.file_B
	
	a = pybedtools.BedTool(fileA).remove_invalid().sort().merge().saveas()
	b = pybedtools.BedTool(fileB).remove_invalid().sort().merge().saveas()
	
	lenght_a = sum([feature.length for feature in a]); print "total length of A:\t", lenght_a
	lenght_b = sum([feature.length for feature in b]); print "total length of B:\t", lenght_b
	print
	a_over_b = a.intersect(b).sort().merge()
	len_of_overlape = sum([feature.length for feature in a_over_b]) ; print "A->B overlape length:\t", len_of_overlape
	b_over_a = b.intersect(a).sort().merge()
	len_of_overlape2 = sum([feature.length for feature in b_over_a]) ; print "B->A overlape length:\t", len_of_overlape2
	print
	print "A - overlap:\t", lenght_a - len_of_overlape
	print "B - overlap:\t", lenght_b - len_of_overlape
	
if __name__ == "__main__":
	try: 
		import timex as tx
		start, startLocal=tx.startTime()
	except: pass
	main()
	try: tx.stopTime(start,startLocal)
	except: pass