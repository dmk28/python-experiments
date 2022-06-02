from ast import Mult
from typing import Any
import numpy as np
import matplotlib as plt
from sympy import *

# A função pede ao usuário que escolha uma das cinco operações.
def multiCalculadora(escolha):
    escolha = input("Por favor, escolha: 'Soma' para soma, 'Sub' para subtração, 'Mult' para multiplicação, 'Div' para divisão, 'Calc1' para derivação.")
    # Match case foi adaptado em Python 3.10. 'Soma', 'Sub', 'Mult', 'Div' e 'Calc1' são as funções dentro da calculadora. Na realidade, até quatro números poderiam ser calculados mas haveria um refatoramento significativo das funções declaradas.
    match escolha:
     case  "Soma":
            somaA = int(input("Digite o primeiro número: "))
            somaB = int(input("Digite o segundo número: "))
            somaTotal = somaA + somaB 
            print("O seu total é", somaTotal)
     case "Sub":
            subA = int(input("Digite o primeiro número: "))
            subB = int(input("Digite o segundo número: "))
            subTotal = subA - subB 
            print("O total é de: ", subTotal)
     case "Mult":
            multA = int(input("Digite o primeiro número. "))
            multB = int(input("Digite o segundo número." ))
            multTotal = multA * multB 
            print("O produto é de: ", multTotal) 
     case "Div":
            divA = int(input("Digite o dividendo." ))
            divB = int(input("Digite o divisor." ))
            divTotal  = divA / divB 
            divModulo = divA % divB 
            if divModulo > 0:
                print("A divisão teve restos: ", divModulo)
                print("O total em decimais é", divTotal)
            else:
                print("O total é,", divTotal)
# Requer numpy, sympy, matplotlib.
     case "Calc1":
               a = int(input("Digite o valor do exponencial."))
               x = Symbol('x')
               funExp = x**a
               derivadaF = funExp.diff(x)
               print(derivadaF)
# Default escrito caso o usuário digite algo errado no prompt, como tratamento de erro.
     case _: 
              print("Inválido.")
              

print(multiCalculadora(escolha=Any))