from operator import truediv
import numpy as np
import getpass
import passlib
from passlib.context import CryptContext

#create CryptContext object
context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=10000
)


def hashPasswords():
   senhaInput=input("Digite a senha a ser criptografada.") 
   novaSenha = context.hash("senhaInput")
   print(novaSenha)
   
  


print(hashPasswords())
