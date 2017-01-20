"""
Python script that creates a file and populates it with random words of 3 characters
Number of words can be programmed
Delimiter between words: \n

In: number of words
Out: file with input number of words

Running instruction:
./make-test-file.py <number-of-words>

Interpretter version: python-2.7.6
Author: Suhas Shrinivasan, dataride; https://bitbucket.org/suhasshrinivasan/
License: PRIVATE, CUSTOM, CLOSED. NON-DISTRIBUTABLE. 
"""

import sys
import random
import string

if len(sys.argv) < 2:
	print "sort.py: expected run instruction - ./make-test-file.py <number-of-words> \naborting"

test_file = open('test-file', 'w')

n = sys.argv[1]	# number of words as command line arguments
for i in range(int(n)):
	word = ''.join(random.choice(string.lowercase) for i in range(3))
	test_file.write(word + '\n')