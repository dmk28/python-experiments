
valorInicial = float(input("Digite o valor inicial"))
taxa_juros_anual = float(input("Digite a taxa de juros: "))
anos = int(input("Digite o número de anos: "))

def calculoJuros(valorInicial: float, taxa_juros_anual:float, anos:int) -> float:
 valorFinal = valorInicial
 for ano in range(1, anos+1):
      valorFinal = valorFinal * (1+taxa_juros_anual)
      valorFinal = round(valorFinal,2)
 print(f'Para um valor inicial de R${valorInicial} ' + \
        f'e uma taxa de juros de {taxa_juros_anual}' + \
        f' em {anos} anos você terá R$ {valorFinal}')
print(calculoJuros(valorInicial, taxa_juros_anual, anos))