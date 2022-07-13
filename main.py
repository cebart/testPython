def voytoletter(src):
    ret = [src]
    for letter in changes:
        buf = ''
        checkdouble = 1
        for c in src:
            if c in voy:
                c = letter
            buf += c
        for r in ret:
            if r == buf:
                checkdouble = 0
        if checkdouble:
            ret.append(buf)
    return ret


word = 'tartuf'
changes = ['i', 'a', 'u', 'y']
voy = ['i', 'a', 'u', 'y', 'e', 'o']
rez = []

rez += voytoletter(word)
for result in rez:
    print(result)

