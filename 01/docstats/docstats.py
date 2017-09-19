# Author: Michelle Beard <Michelle.Beard@tufts.edu>
# StudentID: 1178110

import argparse
import string

from collections import defaultdict

parser = argparse.ArgumentParser(description='Computes how many times each word'
                                             ' occurs in the file, and prints '
                                             'out the top N words.')
parser.add_argument('file',
                    nargs=1,
                    type=str,
                    default='text.txt',
                    help='a text file')
parser.add_argument('n',
                    nargs=1,
                    type=int,
                    default=10,
                    help='top N words')

args = parser.parse_args()

fname = args.file.pop()
n = args.n.pop()

with open(fname) as f:
	content = [w.lower().translate(None, string.punctuation) for line in f for word in line.split() for w in word.split('-')]

result = defaultdict(int)

for word in content:
	result[word] += 1

for i, w in enumerate(sorted(result.items(), key=lambda x: (x[1], x[0]), reverse=True)):
	if i == n: break
	print w[0], w[1]

