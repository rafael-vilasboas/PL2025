from exp_analex import lexer
from exp_ast import Exp, Num, Op, Vazio

prox_simb = ('Erro', '', 0, 0)

def parserError(simb):
    print("Erro sintático, token inesperado: ", simb)

def rec_term(simb):
    global prox_simb
    if prox_simb.type == simb:
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)

# P2: EXPCONT --> '*' EXP
# P3:           | '-' EXP
# P4:           | '+' EXP
# P5:           | ''
def rec_expCont():
    global prox_simb
    if prox_simb == None:
        print("Derivando por P5: EXPCONT --> ''")
        print("Reconheci P5: EXPCONT --> ''")
        op = Vazio('Vazio')
        exp = Vazio('Vazio')
    elif prox_simb.type == 'MUL':
        print("Derivando por P2: EXPCONT --> '*' EXP")
        op = Op('MUL', prox_simb.value)
        rec_term('MUL')
        exp = rec_exp()
        print("Reconheci P2: EXPCONT --> '*' EXP")
    elif prox_simb.type == 'SUB':
        print("Derivando por P3: EXPCONT --> '-' EXP")
        op = Op('SUB', prox_simb.value)
        rec_term('SUB')
        exp = rec_exp()
        print("Reconheci P3: EXPCONT --> '-' EXP")
    elif prox_simb.type == 'ADD':
        print("Derivando por P4: EXPCONT --> '+' EXP")
        op = Op('ADD', prox_simb.value)
        rec_term('ADD')
        exp = rec_exp()
        print("Reconheci P4: EXPCONT --> '+' EXP")
    else:
        parserError(prox_simb)
    return op, exp

# P1: EXP --> NUM EXPCONT
def rec_exp():
    global prox_simb
    if prox_simb.type == 'NUM':
        print("Derivando por P1: EXP --> NUM EXPCONT")
        num = Num('NUM', prox_simb.value)
        rec_term('NUM')
        op, exp = rec_expCont()
        print("Reconheci P1: EXP --> NUM EXPCONT")
    else:
        parserError(prox_simb)
    return Exp('EXP', num, op, exp)

def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    res = rec_exp()
    res.pp()
