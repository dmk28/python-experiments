import this
from unittest import result

#test method
# anos = [2, 4, 5, 2, 10, 15, 8]
# juros = [0.02, 0.05, 0.045, 0.35, 0.25, 0.35, 0.20]
# valor_inicial = [3000, 4500, 6000, 3500, 5500, 6500, 4000]

#reading file
content = []
lista_anos = []
lista_juros = []
lista_valor_inicial = []
with open(file='./juros.csv', mode='r') as file_juros:
   this_line = file_juros.readline()
   this_line = file_juros.readline()
   while this_line: 
    separate_line = this_line.split(sep=',')
    anos = separate_line[0]
    anos = int(anos)
    lista_anos.append(anos)
    juros = separate_line[1]
    juros = float(juros)
    lista_juros.append(juros)
    valor_inicial = separate_line[2]
    valor_inicial = float(valor_inicial)
    lista_valor_inicial.append(valor_inicial)
    content.append(this_line)
    this_line = file_juros.readline()
print(content)



def retorno(valor_inicial: float, juros: float, anos: int) -> float:
    valor_final = valor_inicial
    for ano in range(1, anos+1):
        valor_final = valor_final * (1 + juros)
    return round(valor_final,2)

# opções = list(map(retorno, valor_inicial, juros, anos))
opções = list(map(retorno, lista_valor_inicial, lista_juros, lista_anos))

def escolha_impressao():
    numero_de_dados = len(opções)
    print(f'Existem {numero_de_dados} posições de dados a serem lidas. Qual gostaria de ler?')
    escolha = int(input("Digite a posição: "))
    print(opções[escolha])

escolha_impressao()


