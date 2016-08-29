# O while executa um comando enquanto o argumento possuir um valor de verdade 
# igual à True.
#
# No loop abaixo, enquanto x for menor que 5, o valor de verdade da expressão 
# "x > 5" será verdadeiro. Neste caso, imprimimos os números de 1 a 5
x = 0
while x < 5:
    x += 1
    print('x = %s' % x)

# Note que essas formas são válidas:
#
# >>> while True:
# ...     <comando a ser executado indefinidamente>
#
# Versão alternativa do anterior
#
# >>> while 1:
# ...     <comando a ser executado indefinidamente>
#
# Não faz muito sentido, mas sintaticamente válido
#
# >>> while False:
# ...     <comando que nunca será executado>
#
#
# Exercícios 
# ----------
#
# 1) Faça um programa que calcule o produto dos números de 1 à 10 utilizando 
#    o laço while.
#
# 2) Faça um programa que calcule o fatorial de 20  utilizando 
#    o laço while.

