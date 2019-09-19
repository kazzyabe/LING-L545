import sys
from wer import wer

g_truth = open("ground_truth.txt")
maxmatch = open("mm_result.txt")

g = g_truth.readline()
m = maxmatch.readline()

# taking mean
c = 1
numorator = 0
while m and g:
    numorator += float(wer(g,m))
    g = g_truth.readline()
    m = maxmatch.readline()
    c += 1

g_truth.close()
maxmatch.close()
print(numorator/c)