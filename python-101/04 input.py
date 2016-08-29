# A função input() pede uma entrada para o usuário
# É interessante forçar o tipo certo (por exemplo, chamando a função int() para
# garantir que a saída é um número inteiro)
x = int(input('Digite um número: '))

# Responde de acordo com a entrada do usuário
print('%s, ganhei!' % (x + 1))

# Observalção 1: alguns programas (ex.: gedit) não funcionam corretamente com 
# scripts que pedem entrada do usuário. Neste caso é necessário invocar o 
# programa do terminal chamando "python3 <nome do arquivo>"
#
# Observação 2: o comportamento de input() mudou do python2 para o python3. 
# No primeiro é sempre aconselhável usar a função raw_input(), que retorna uma
# string. No python3, a função input() possui o mesmo comportamento da 
# raw_input() do python2.
#
# Exercícios 
# ----------
#
# 1) Faça um programa que pergunte um número inteiro para o usuário e imprima
#    na tela o seu fatorial.
#
