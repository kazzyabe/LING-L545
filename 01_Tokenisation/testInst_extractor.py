import sys

f = open("UD_Japanese-GSD-master/ja_gsd-ud-test.conllu")

line = f.readline()
while line:
    if "# text = " in line and line[0] != '\n':
        line = line.split("# text = ")
        sys.stdout.write(line[1])
    line = f.readline()

f.close()