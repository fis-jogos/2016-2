# A função input() pede uma entrada para o usuário
x = int(input('Digite um número: '))

# Executamos mensagens diferentes dependendo do número escolhido. 
# O bloco if, elif, else executa apenas o primeiro bloco que satisfaz a condição
# dada. Tanto os elif, quanto o else são opcionais.
if x == 0:
    print('Não gosto de zero!')
elif x % 2 == 0:
    print('Número par, boa escolha.')
elif x > 10:
    print('Número ímpar, mas muito grande.')
else:
    print('Número ímpar, de bom tamanho.')

#    
# Exercícios 
# ----------
#
# 1) Escreva um número de 1 a 100 numa variável. Agora faça um programa que peça
#    para o usuário advinhar este número e só termine a execução quando o 
#    usuário acertar o número correto. O programa deve retornar dicas do tipo
#    "tente um número menor" ou "tente um número maior"
#

