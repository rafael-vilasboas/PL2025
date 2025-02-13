def geraCombinacoesMaiusculaMinuscula(palavra: str, prefixo: str, n: int, resultado: list[str]):
    if (n == len(palavra)):
        resultado.append(prefixo)
    else:
        novoPrefixoMaiusculo = prefixo + palavra[n].lower()
        novoPrefixoMinusculo = prefixo + palavra[n].upper()
        geraCombinacoesMaiusculaMinuscula(palavra, novoPrefixoMaiusculo, n + 1, resultado)
        geraCombinacoesMaiusculaMinuscula(palavra, novoPrefixoMinusculo, n + 1, resultado)

palavras_on = list()
geraCombinacoesMaiusculaMinuscula("on", "", 0, palavras_on)
palavras_off = list()
geraCombinacoesMaiusculaMinuscula("off", "", 0, palavras_off)

ficheiro = open("teste.txt", 'w')

for palavra in palavras_on:
    ficheiro.write(palavra + " 1 = off\n")

ficheiro.write("on 10 =\n")

for palavra in palavras_off:
    ficheiro.write("on " + palavra + " 1 =\n")
