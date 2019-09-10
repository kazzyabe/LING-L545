import sys

f = open("UD_Japanese-GSD-master/ja_gsd-ud-train.conllu")

line = f.readline()
while line:
    if line[0] != '#' and line[0] != '\n':
        line = line.split('\t')
        sys.stdout.write(line[1] + '\n')
    line = f.readline()

f.close()