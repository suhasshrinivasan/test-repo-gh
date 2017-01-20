"""
Script will test if a file has contents alphabetically sorted
Delimiter between contents: \n

In: file consisting of words
Out: boolean: if sorted, True; else, False

Running instructions:
./is-sorted.py <path-to-file>

Interpretter version: python-2.7.6
Author: Suhas Shrinivasan, dataride; https://bitbucket.org/suhasshrinivasan/
License: PRIVATE, CUSTOM, CLOSED. NON-DISTRIBUTABLE. 
"""

import sys

def is_sorted(input_file):
	lines = input_file.readlines()
	if all(lines[i] <= lines[i + 1] for i in range(len(lines) - 1)):
		print "is-sorted: TRUE"
	else:
		print "is-sorted: FALSE" 

def main():
	if len(sys.argv) < 2:
		print "is-sorted.py: expected run instruction - ./is-sorted.py <path-to-file> \naborting"
	input_file = open('test-file', 'r')
	is_sorted(input_file)

if __name__ == '__main__':
	main()