# Author: Michelle Beard <Michelle.Beard@tufts.edu>
# StudentID: 1178110

import argparse

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