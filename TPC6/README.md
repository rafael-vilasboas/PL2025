# TPC5
## 2025-03-17

**Nome** José Rafael de Oliveira Vilas Boas

**Número** A76350

**Foto** ![Foto](../foto.jpg)

## Introdução

Criação de um programa com análise léxica e sintática de expressões numéricas com subtrações e multiplicações.

## Análise Léxica

### Tokens

Foram identificados os seguintes tokens

```python
    tokens = [
      'NUM',  # Número
      'MUL',  # Multiplicação
      'SUB',  # Subtração
      'ADD'   # Adição
    ]
```

Com as seguintes regras de identificação

```python
  t_NUM = r'\d+'  # Números inteiros
  t_MUL = r'\*'   # Sinal multiplicação
  t_SUB = r'\-'   # Sinal subtração
  t_ADD = r'\+'   # Sinal adição
```

## Análise Sintática

### Gramática

Foram identificados os seguintes conjuntos de símbolos não terminais, N, e símbolos terminais, T, símbolo inicial, S, e regras de produção, P

```python
  T = { 'NUM', '*', '-', '+' }
  N = { 'EXP', 'EXPCONT' }
  S = 'EXP'
  P = {
    'EXP' --> 'NUM' 'EXPCONT' # P1
    'EXPCONT' --> '*' 'EXP'   # P2
                | '-' 'EXP'   # P3
                | '+' 'EXP'   # P4
                | ''  'EXP'   # P5
  }
```

## Utilização

Correr no terminal o seguinte comando

```bash
    $ py exp_program.py
```
