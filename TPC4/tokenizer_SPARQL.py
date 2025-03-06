
import sys
import re

def tokenize(input_string):
    reconhecidos = []
    linha = 1
    mo = re.finditer(r'(?P<SELECT>[sS][eE][lL][eE][cC][tT])|(?P<WHERE>[wW][hH][eE][rR][eE])|(?P<LIMIT>[lL][iI][mM][iI][tT])|(?P<NUM>\d+)|(?P<PA>{)|(?P<PF>})|(?P<ID>\?[a-z]\w*)|(?P<PROPERTY>\w+:\w+)|(?P<VALUE>\".+\")|(?P<LANG>@\w+)|(?P<TYPE>(a|rdf:type))|(?P<POINT>\.)|(?P<NEWLINE>\n)|(?P<SKIP>[ \t]+)|(?P<ERRO>.)', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['SELECT']:
            t = ("SELECT", dic['SELECT'], linha, m.span())

        elif dic['WHERE']:
            t = ("WHERE", dic['WHERE'], linha, m.span())
    
        elif dic['LIMIT']:
            t = ("LIMIT", dic['LIMIT'], linha, m.span())
    
        elif dic['NUM']:
            t = ("NUM", dic['NUM'], linha, m.span())
    
        elif dic['PA']:
            t = ("PA", dic['PA'], linha, m.span())
    
        elif dic['PF']:
            t = ("PF", dic['PF'], linha, m.span())
    
        elif dic['ID']:
            t = ("ID", dic['ID'], linha, m.span())
    
        elif dic['PROPERTY']:
            t = ("PROPERTY", dic['PROPERTY'], linha, m.span())
    
        elif dic['VALUE']:
            t = ("VALUE", dic['VALUE'], linha, m.span())
    
        elif dic['LANG']:
            t = ("LANG", dic['LANG'], linha, m.span())
    
        elif dic['TYPE']:
            t = ("TYPE", dic['TYPE'], linha, m.span())
    
        elif dic['POINT']:
            t = ("POINT", dic['POINT'], linha, m.span())
    
        elif dic['NEWLINE']:
            t = ("NEWLINE", dic['NEWLINE'], linha, m.span())
    
        elif dic['SKIP']:
            t = ("SKIP", dic['SKIP'], linha, m.span())
    
        elif dic['ERRO']:
            t = ("ERRO", dic['ERRO'], linha, m.span())
    
        else:
            t = ("ERRO", m.group(), linha, m.span())
        if not dic['SKIP']: reconhecidos.append(t)
    return reconhecidos

for linha in sys.stdin:
    for tok in tokenize(linha):
        print(tok)

