# cat wiki.txt|python segmenter.py| more
# cat wiki.txt | grep --colour ' [a-z]\+\.' for abreviation

import sys

line = sys.stdin.readline()
while line != '':
    for c in '?!.':
        line = line.replace(c, c + '\n\n')
    sys.stdout.write(line)
    line = sys.stdin.readline()