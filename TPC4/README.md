# TPC4
## 2025-03-02

**Nome** José Rafael de Oliveira Vilas Boas

**Número** A76350

**Foto** ![Foto](../foto.jpg)

## Introdução

Criação de um analisador léxico para um exemplo da linguaguem query SPARQL.

### Exemplo

Exemplo no ficheiro [teste.txt](teste.txt)

```python
    select ?nome ?desc where {
        ?s a dbo:MusicalArtist.
        ?s foaf:name "Chuck Berry"@en .
        ?w dbo:artist ?s.
        ?w foaf:name ?nome.
        ?w dbo:abstract ?desc
    } LIMIT 1000
```

## Tokens

Os tokens dentificados e as suas expressões regulares são as seguintes:

```python
    token_specification = [
        ('SELECT',    r'[sS][eE][lL][eE][cC][tT]'),
        ('WHERE',     r'[wW][hH][eE][rR][eE]'),
        ('LIMIT',     r'[lL][iI][mM][iI][tT]'),
        ('NUM',       r'\d+'),
        ('PA',        r'\{'),
        ('PF',        r'\}'),
        ('ID',        r'\?[a-z]\w*'),
        ('PROPERTY',  r'\w+:\w+'),
        ('TYPE',      r'(a|rdf:type)'),
        ('POINT',     r'\.'),
        ('NEWLINE',   r'\n'),
        ('SKIP',      r'[ \t]+'),
        ('ERRO',      r'.')
    ]
```

## Utilização

Correr o programa no terminal com:

``` bash
$ py tokenizer_SPARQL
```
