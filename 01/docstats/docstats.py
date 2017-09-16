# Author: Michelle Beard <Michelle.Beard@tufts.edu>
# StudentID: 1178110

import argparse
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
	content = [word for line in f for word in line.split()]

result = defaultdict(int)

for word in content:
	result[word] += 1

for i, w in enumerate(sorted(result, key=result.get, reverse=True)):
	if i == n: break
	print w, result[w]
