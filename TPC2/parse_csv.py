import sys

def print_obras(obras):
    for obra in obras:
        print(f'obra: {obra}')
        for valor in cabecalho:
            if valor != col_id:
                print(f'{valor}: {obras[obra][valor]}')

def parse_header(linha: str) -> list[str]:
    valores = []
    string = ""
    for caractere in linha:
        if caractere == ';' or caractere == '\n':
            valores.append(string)
            string = ""
        else:
            string += caractere
    return valores

obras = {}

lista_compositores = []
map_obras_periodo = {}
map_obras_catalogadas_periodo = {}

if len(sys.argv) != 3:
    print("Número de argumentos inválido")
    sys.exit()

file_path = sys.argv[1]

col_id = sys.argv[2]

try:
    file = open(file_path, 'r', encoding='utf-8')
except:
    print("Não foi possível abrir o ficheiro")
    sys.exit()

header = file.readline()
cabecalho = parse_header(header)
print(cabecalho)
n = len(cabecalho) - 1
id = 0

while id <= n and cabecalho[id] != col_id:
    id += 1

valores = {}
string = ""
i = 0
texto = False

for linha in file:
    for caractere in linha:
        if caractere == '"':
            texto = not texto
        if caractere == ';' and not texto:
            valores[cabecalho[i]] = string
            i += 1
            string = ""
        elif i == n and caractere == '\n':
            i = 0
            obras[string] = valores
            string = ""
            valores = {}
        else:
            string += caractere

for obra in obras.values():
    lista_compositores.append(obra["compositor"])
    periodo = obra["periodo"]
    if (periodo not in map_obras_periodo):
        map_obras_catalogadas_periodo[periodo] = 0
        map_obras_periodo[periodo] = []
    map_obras_catalogadas_periodo[periodo] += 1
    map_obras_periodo[periodo].append(obra["nome"])

lista_compositores.sort()
for obras in map_obras_periodo.values():
    obras.sort()

for compositor in lista_compositores:
    print(compositor)

for (periodo, obras) in map_obras_periodo.items():
    print(periodo + ": " + str(obras))
