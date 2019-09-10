from nltk.tokenize import sent_tokenize
import sys

line = sys.stdin.readline()
while line != '':
    line = sent_tokenize(line)
    for l in line:
        sys.stdout.write(l + '\n\n')
    line = sys.stdin.readline()