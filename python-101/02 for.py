# Vamos imprimir os números pares de 0 à 10 e a sua soma
print('Primeiros números pares:')
soma = 0

# O laço tipo "for" é sempre realizado em cima de uma sequência
# Observe que o bloco de execução é definido por identação
for x in range(0, 12, 2):
    soma += x
    print(' %s' % x)

print('Soma: %s' % soma)

# Nota: A função range(a, b, c) cria uma iteração que inicia em "a", termina 
# antes de "b" e incrementa de "c" em "c". Deste modo, 
# range(0, 12, 2) ==> [0, 2, 4, 6, 8, 10]
#
# As versões com 1 ou 2 argumentos possuem as equivalências:
#   range(x) <==> range(0, x, 1)
#   range(x, y) <==> range(x, y, 1)
#
# Nota 2: Aqui usamos o laço "for" para realizar somas. A maneira idiomática (e
# muito mais simples) de fazer isto seria utilizar a função sum() que soma os
# termos de uma lista:
#
#    soma = sum(range(0, 12, 2))
#
# Exercícios 
# ----------
#
# 1) Faça um programa que calcule o produto dos números de 1 à 10
#
# 2) Faça um programa que calcule o fatorial de 20
#
