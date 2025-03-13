# TPC5
## 2025-03-09

**Nome** José Rafael de Oliveira Vilas Boas

**Número** A76350

**Foto** ![Foto](../foto.jpg)

## Introdução

Criação de um programa com funcionalidade de uma máquina de venda automática, utilizando `ply lex` para fazer a análise léxica e responder aos pedidos de acordo com essa análise.

## Tokens

Para isso foram identificados os seguintes tokens

```python
    tokens = [
        "LISTAR",       # Comando listar
        "MOEDA",        # Comando moeda
        "MOEDAEURO",    # Moeda de euro
        "MOEDACENTIMO", # Moeda de centimo
        "FIMCOMPRA",    # Fim de depósito de moeda
        "SELECIONAR",   # Comando selecionar
        "PRODUTO",      # Produto selecionado
        "FIMPEDIDO",    # Fim de pedido de produto
        "SAIR"          # Comando sair
    ]
```

## Estados

E os seguintes estados

```python
    states = [
        ("COMPRA", "exclusive"),            # Estado de compra
        ("SELECIONARPRODUTO", "exclusive")  # Estado de seleção
    ]
```

Em que em cada estado estão associados os seguintes tokens

    INITIAL
    + LISTAR - Comando de listagem dos produtos
    + MOEDA - Comando de inicialização de depósito de moedas
      + Inicializa o estado COMPRA
    + SELECIONAR - Comando de inicialização da seleção do produto
      + Inicializa o estado SELECIONARPRODUTO
    + SAIR - Comando de fim da compra

    COMPRA
    + MOEDAEURO - Identifica uma moeda de euro
    + MOEDACENTIMO - Identifica uma moeda de centimo
    + FIMCOMPRA - Identifica o fim deste estado
      + Inicializa o estado INITIAL

    SELECIONARPRODUTO
    + SELECIONAR - Comando de seleção do produto
    + PRODUTO - Identifica o produto
    + FIMPEDIDO - Identifica o fim deste estado
      + Inicializa o estado INITIAL

## Utilização

Correr no terminal o seguinte comando

```bash
    $ py maq_vending.py stock.json
```
