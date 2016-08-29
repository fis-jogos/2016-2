# Definimos uma função que calcula a soma de todos os números pares até um
# certo valor
def soma_pares(x):
    y = 0
    S = 0
    while y <= x:
        S += y
        y += 2
    return y
       
# Agora podemos chamar nossa função e recuperar o valor passado para o "return"
valor = soma_pares(100)
print('A soma de todos os pares de 1 a 100 é: %s' % valor)
       
# Exercícios 
# ----------
#
# 1) Defina uma função que calcule o fatorial de um número. 
#
# 2) Faça um programa que pergunte para o usuário o fatorial do número e depois
#    imprima o resultado. O programa deve utilizar a função definida 
#    anteriormente e deve continuar perguntando por mais números até que o 
#    usuário entre com o valor 0.
