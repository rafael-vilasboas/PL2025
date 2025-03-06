import sys
import json

file = sys.argv[1]

tokens = []
with open(file) as f:
    tokens = json.load(f)

tokens_regex = '|'.join([f'(?P<{t['id']}>{t['expreg']})' for t in tokens])

code = f"""
import sys
import re

def tokenize(input_string):
    reconhecidos = []
    linha = 1
    mo = re.finditer(r'{tokens_regex}', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['{tokens[0]['id']}']:
            t = ("{tokens[0]['id']}", dic['{tokens[0]['id']}'], linha, m.span())
"""

for t in tokens[1:]:
    code += f"""
        elif dic['{t['id']}']:
            t = ("{t['id']}", dic['{t['id']}'], linha, m.span())
    """

code += f"""
        else:
            t = ("ERRO", m.group(), linha, m.span())
        if not dic['SKIP']: reconhecidos.append(t)
    return reconhecidos

for linha in sys.stdin:
    for tok in tokenize(linha):
        print(tok)
"""
print(code)
