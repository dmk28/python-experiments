nomeLoginCheck = "tokyoGhoul" #@param {type:"string"}
senhaEntrada = "be4utifulW0rld" #@param {type:"string"}

from operator import truediv
import numpy as np
import getpass

nomeLogin = 'tokyoGhoul'
senhaLogin = 'be4utifulW0rld!'


def loggingIn(nomeLoginCheck, senhaEntrada):
    nomeLoginCheck = str(input("Por favor, digite o login."))
    print(nomeLoginCheck)
    senhaEntrada = getpass.getpass("Entre com a senha.")
        
    if nomeLoginCheck == nomeLogin and senhaEntrada == senhaLogin:
      matchPass = True
      print("Bem vindo ao sistema.")
    elif nomeLoginCheck != nomeLogin or senhaEntrada != senhaLogin:
      matchPass = False
      print("Senha e/ou usuário errado, tente novamente")
    return matchPass
print(loggingIn(nomeLoginCheck, senhaEntrada))

