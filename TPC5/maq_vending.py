import sys
from datetime import date
import json
import ply.lex as lex
import re

tokens = ["LISTAR", "MOEDA", "MOEDAEURO", "VIRG", "MOEDACENTIMO", "FIMCOMPRA", "SELECIONAR", "PRODUTO", "FIMPEDIDO", "SAIR", "SKIP"]

states = [("COMPRA", "exclusive"), ("SELECIONARPRODUTO", "exclusive")]

def t_LISTAR(t):
    r'^[Ll][Ii][Ss][Tt][Aa][Rr]$'
    return t

def t_MOEDA(t):
    r'^[Mm][Oo][Ee][Dd][Aa]'
    t.lexer.begin("COMPRA")
    return t

def t_COMPRA_MOEDAEURO(t):
    r'(1|2)e'
    t.value = float(re.split('e', t.value)[0])
    t.lexer.saldo += t.value
    return t

def t_COMPRA_MOEDACENTIMO(t):
    r'(50|20|10|5)c'
    t.value = float(re.split('c', t.value)[0]) / 100
    t.lexer.saldo += t.value
    return t

def t_COMPRA_FIMCOMPRA(t):
    r'\.'
    saldo = re.split(r'\.', "{:.2f}".format(t.lexer.saldo))
    print(f'Saldo = {saldo[0]}e{saldo[1]}c')
    t.lexer.begin("INITIAL")
    return t

def t_SELECIONAR(t):
    r'^[Ss][Ee][Ll][Ee][Cc][Ii][Oo][Nn][Aa][Rr]'
    t.lexer.begin("SELECIONARPRODUTO")
    return t

def t_SELECIONARPRODUTO_PRODUTO(t):
    r'A(\d+)'
    produto = None
    for p in t.lexer.stock:
        if p['cod'] == t.value:
            produto = p
    if produto:
        if produto['quant'] <= 0:
            print("Não existe stock suficiente")
        elif t.lexer.saldo < produto['preco']:
            print("Saldo insuficiente para satizfazer o seu pedido")
            saldo = re.split(r'\.', "{:.2f}".format(t.lexer.saldo))
            pedido = re.split(r'\.', "{:.2f}".format(produto['preco']))
            if t.lexer.saldo >= 1:
                print(f'Saldo = {saldo[0]}e{saldo[1]}c; Pedido = {pedido[0]}e{pedido[1]}c')
            else:
                print(f'Saldo = {saldo[1]}c; Pedido = {pedido[0]}e{pedido[1]}c')
        else:
            print(f'Pode retirar o produto dispensado {produto['nome']}')
            t.lexer.saldo -= produto['preco']
            saldo = re.split(r'\.', "{:.2f}".format(t.lexer.saldo))
            print(f'Saldo = {saldo[0]}e{saldo[1]}c')
    else:
        print("Produto não existe")
    return t

def t_SELECIONARPRODUTO_FIMPEDIDO(t):
    r'\n'
    t.lexer.begin("INITIAL")
    return t

def t_SAIR(t):
    r'^[Ss][Aa][Ii][Rr]$'
    saldo = re.split(r'\.', "{:.2f}".format(t.lexer.saldo))
    print(f'Pode retirar o troco: {saldo[0]}e{saldo[1]}c')
    print('Até à próxima')
    return t

def t_COMPRA_VIRG(t):
    r'\,'
    return t

def t_ANY_SKIP(t):
    r'[ \t]+'
    pass

def t_ANY_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value[0])

def t_ANY_error(t):
    print(f'Erro: {t.value[0]}')
    t.lexer.skip(1)

def carrega_stock():
    with open("stock.json") as json_stock:
        stock = json.load(json_stock)
    return stock["stock"]

lexer = lex.lex()
lexer.saldo = 0.0
lexer.stock = carrega_stock()

data = date.today()
print(f'{data}, Stock carregado, Estado atualizado.')
print("Bom dia. Estou disponível para atender o seu pedido.")

for l in sys.stdin:
    lexer.input(l)
    for tok in lexer:
        continue
