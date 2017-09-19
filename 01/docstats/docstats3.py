# Author: Michelle Beard <Michelle.Beard@tufts.edu>
# StudentID: 1178110

import argparse
import string

from collections import defaultdict

parser = argparse.ArgumentParser(description='Compute the sentiment of the text '
                                             'in the first file using the second'
                                             ' file as the sentiment lexicon, '
                                             'and prints out the sentiment of '
                                             'the first file.')
parser.add_argument('file',
                    nargs=1,
                    type=str,
                    default='text.txt',
                    help='a text file')

parser.add_argument('lexicon',
                    nargs=1,
                    type=str,
                    default='lexicon.txt',
                    help='a text file')

args = parser.parse_args()

fname = args.file.pop()
lname = args.lexicon.pop()

lexicon = defaultdict(int)

with open(lname) as f:
	for line in f:
		key, val = line.split()
		lexicon[key] = int(val)


with open(fname) as f:
	content = [w.lower().translate(None, string.punctuation) for line in f for word in line.split() for w in word.split('-')]

c = reduce(lambda x, key: x + lexicon[key], content, 0)

print('The sentiment of file %s is %d' % (fname, c))