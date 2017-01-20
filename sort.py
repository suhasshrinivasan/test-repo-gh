"""
Sorts file contents alphabetically 
Delimeter between contents: \n
Pipeline test 

In: regular file containing text
Out: sorted input file

Run instruction:
./sort-file.py <path-to-file>

Warning: in-memory sorting

Interpretter version: python-2.7.6
Author: Suhas Shrinivasan, dataride; https://bitbucket.org/suhasshrinivasan/
License: PRIVATE, CUSTOM, CLOSED. NON-DISTRIBUTABLE. 
"""

import sys

def file_sort(input_file):
	lines = sorted(input_file.readlines())
	input_file.seek(0)
	input_file.truncate()
	for line in lines:
		input_file.write(line)

def main():
	if len(sys.argv) < 2:
		print "sort.py: expected run instruction - ./sort-file.py <path-to-file> \naborting"

	input_file = open("test-file", 'r+')
	file_sort(input_file)

if __name__ == '__main__':
	main()