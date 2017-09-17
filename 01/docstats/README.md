Author: Michelle Beard

StudentID: 1178110

Sentiment Extractor
===================
Small scripts to compute word counts and sentiment values. 

How to Run Application
----------------------
1. Compute how many times each word occurs in a file, and prints out the top N words.
   ```
   $ python docstats.py text.txt 10
   ```
1. Compute how many times each word occurs in the first file ignoring the stop words 
   listed in the second file, and print out the top N words.
   ```
   $ python docstats2.py text.txt stopwords.txt 10
   ```
1. Computes the sentiment of the text in the first file using the second file as 
   the sentiment lexicon, and prints out the sentiment of the first file.
   ```
   $ python docstats3.py text.txt lexicon.txt
   ```
