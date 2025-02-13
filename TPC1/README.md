# TCP1
## 2025-02-10

* **Nome** José Rafael de Oliveira Vilas Boas
* **Número** A76350
* **Foto** ![Foto](../foto.jpg)

## Introdução

Implementação de um somador on/off para resolução do TCP1 de processamento de linguagens.

O programa [somador.py](./somador.py) soma todas as sequências de digitos num texto, sendo que esta função pode ser ativada e desativada com a string "On" e "Off" (com qualquer combinação de maiúsculas e minúsculas) e pode ser imprimido o resultado da soma atual com o caracter "=".

## Utilização

Ao correr o programa no terminal este fica à espera de input no stdin, de seguida pode ser escrita uma linha, dando o input, e quando for introduzida uma nova quebra de linha o programa devolde o output, caso exista, dessa linha. O programa termina com a introdução do carater de EOF.

Exemplo de demonstração:
```
py somador.py
On = 1 abc = 2 = Off 1 1 =
0
1
3
3
```

Também é possível redirecionar o conteúdo num ficheiro para o stdin do programa, da seguinte forma:

```
py somador.py < teste.txt
```

Ainda pode ser passado ao programa o ficheiro a redirecionar como primeiro argumento:

```
py somador.py teste.txt
```

## Resultados

Com o programa [gera_teste.py](gera_teste.py) pode ser gerado um ficheiro de texto, ``teste.txt`` com alguns testes para verificar o correto funcionamento do programa [somador.py](somador.py).

No ficheiro ``teste.txt`` são primeiro testadas as somas e combinações da palavra ``on``, devendo ser imprimido um número incrementado por um valor a cada linha, de seguida são testadas as combinações da palavra ``off``, devendo ser imprimido o mesmo número até ao fim do ficheiro.

Executando o programa [somador.py](somador.py) com o ficheiro ``teste.txt`` é obtido o seguinte output correspondente ao correto funcionamento do programa:

```
py somador.py < teste.txt
1
2
3
4
14
14
14
14
14
14
14
14
14
```
