# Author: Michelle Beard <Michelle.Beard@tufts.edu>
# StudentID: 1178110

import argparse
import string

from collections import defaultdict

parser = argparse.ArgumentParser(description='Compute how many times each word '
											 'occurs in the first file, ignoring'
											 ' the stop words listed in the '
                                             'second file, and print out the '
                                             'top N words.')

parser.add_argument('file',
                    nargs=1,
                    type=str,
                    default='text.txt',
                    help='a text file')

parser.add_argument('stopwords',
                    nargs=1,
                    type=str,
                    default='stopwords.txt',
                    help='a text file')

parser.add_argument('n',
                    nargs=1,
                    type=int,
                    default=10,
                    help='top N words')

args = parser.parse_args()

fname = args.file.pop()
sname = args.stopwords.pop()
n = args.n.pop()

with open(sname) as f:
	stopwords = [word for line in f for word in line.split()]

with open(fname) as f:
	content = [w.lower().translate(None, string.punctuation) for line in f for word in line.split() for w in word.split('-')]

s_content = list(filter(lambda w: w not in stopwords, content))

result = defaultdict(int)

for word in s_content:
	result[word] += 1

for i, w in enumerate(sorted(result.items(), key=lambda x: (x[1], x[0]), reverse=True)):
	if i == n: break
	print w[0], w[1]
