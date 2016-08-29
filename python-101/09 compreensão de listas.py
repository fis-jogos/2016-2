# O Python possui uma notação elegante para criar listas que podem ser geradas
# de maneira simples em uma única linha, sem utilizar um laço de for.
#
# São as chamadas compreensões de lista. No exemplo vamo criar uma lista de
# quadrados perfeitos utilizando um for:
L = []
for i in range(10):
    L.append(i**2)
    
# Podemos obter o mesmo efeito em uma única linha com a notação abaixo
L = [i**2 for i in range(10)]

# A compreensão de lista também permite filtrar termos, acrescentando uma
# cláusula if no final
L = [i**2 for i in range(10) if i % 2 == 0]   # filtra apenas os índices pares

# Exercícios
# ----------
#
# 1) Escreva um programa de uma única linha que imprime a soma dos cubos dos 
#    números de 1 a 10.
#
    


