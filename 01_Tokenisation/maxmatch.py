def maxmatch(string, dictionary):
    if len(string) == 1:
        return [string]
    else:
        for i in range(len(string)-1, -1, -1):
            w = string[:i+1]
            rem = string[i+1:]
            if w in dictionary:
                # print(w)
                return [w] + maxmatch(rem,dictionary)
            elif w == " ":
                return maxmatch(rem, dictionary)
            elif len(w) == 1:
                return [w] + maxmatch(rem,dictionary)

def load_dictionary(f = 'Dictionary_uniq.txt'):
    f = open(f,'r')
    dictionary = []
    w = f.readline()
    while w:
        w = w.strip()
        dictionary += [w]
        w = f.readline()
    return dictionary

# s = "次は夜にちょい飲みで行こうかな"

if __name__ == "__main__":
    import sys
    dictionary = load_dictionary()

    f = open("test.txt", "r")
    s = f.readline().strip()
    c = 1
    while s:
        sys.stdout.write("///".join(maxmatch(s,dictionary)) + "\n")
        s = f.readline().strip()
        c = c + 1 