import sys
from wer import wer

g_truth = open("ground_truth.txt")
maxmatch = open("mm_result.txt")

g = g_truth.readline()
m = maxmatch.readline()

while m and g:
    sys.stdout.write(wer(g,m) + "\n")
    g = g_truth.readline()
    m = maxmatch.readline()

g_truth.close()
maxmatch.close()