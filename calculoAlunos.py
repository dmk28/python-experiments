quadroAlunos = {}

#nesse exercício, é necessário utilizar a recursividade para poder cumprir os parâmetros básicos do enunciado

def atualizarCadastroAluno():
   perguntaAluno = input("Qual seria o nome do aluno?")
   perguntaNotaUm = float(input("Qual seria sua primeira nota?"))
   perguntaNotaDois = float(input("Qual seria sua nota dois?"))
#as perguntas são feitas nos tipos de dado string, float e float
   mediaAluno = (perguntaNotaUm + perguntaNotaDois) / 2
   #a media é a soma das notas, dividido por dois
   quadroAlunos.update({perguntaAluno:mediaAluno})
   #o dicionário, tipo de dados mais adequado para esse tipo de coisa  no Python, é atualizado
   perguntaContinuar = input("Deseja continuar? S para sim, N para não. ")
   #aqui, essa pergunta determina a recursividade da função
   if (perguntaContinuar == 'S'):
     atualizarCadastroAluno()
     #observe que a função se chama novamente para fazer as mesmas perguntas
   elif (perguntaContinuar == 'N'):
     print("A média dos seus alunos, listada em ordem, é de: ", quadroAlunos)
     return mediaAluno
   else:
     #se o usuário digitar algo errado...
     print("Resposta inválida, execute o programa novamente. A média dos alunos até agora é de: ", quadroAlunos)
     return mediaAluno

atualizarCadastroAluno()