import sys

f = open("UD_Japanese-GSD-master/ja_gsd-ud-test.conllu")

line = f.readline()
extract = False
g_t = ""

while line:
    if "# text = " in line:
        # print("start")
        extract = True
        g_t = ""
    elif line[0] == '\n':
        # print("end")
        extract = False
        sys.stdout.write(g_t + '\n')

    if extract and not("# text = " in line):
        line = line.split('\t')
        # print(line)
        g_t = g_t + " " + line[1]
        # print(g_t)

    line = f.readline()

f.close()