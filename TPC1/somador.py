import sys

def rec_soma(l: str, s: int, on: bool):
    i = 0
    while i < len(l):
        if l[i] in "oO" and (i+1) < len(l):
            i += 1
            if l[i] in "nN":
                on = True
            elif l[i] in "fF" and (i+1) < len(l) and l[i+1] in "fF":
                i += 2
                on = False
        if on and l[i] in "0123456789":
            n = 0
            while l[i] in "0123456789":
                n = n * 10 + int(l[i])
                i += 1
            s += n
        if l[i] == '=':
            print(s)
        i += 1
    return (s, on)

soma = 0
on = False
if len(sys.argv) > 1 and sys.argv[1] != '<':
    try:
        ficheiro = open(sys.argv[1], 'r')
        for linha in ficheiro:
            (soma, on) = rec_soma(linha, soma, on)
    except:
        sys.exit("ERROR. Segundo argumento deve ser o nome do ficheiro")
else:
    for linha in sys.stdin:
        (soma, on) = rec_soma(linha, soma, on)
