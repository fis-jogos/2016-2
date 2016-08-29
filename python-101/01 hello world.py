# Este programa fala "Hello" para uma tupla de nomes
nomes = ("João", "Maria", "José", "Jesus")

# Junta todos os nomes, menos o último numa string
nomes_aux = nomes[:-1]
nomes_aux = ', '.join(nomes_aux)

# Imprime uma mensagem na tela
string_formatada = "Hello %s and %s" % (nomes_aux, nomes[-1])
print(string_formatada)

#
# Observe que o operador de formatação "%" funciona de maneira parecida com a
# função printf() do C. Note que no python não é necessário atribuir o tipo da 
# variável explicitamente (%i, %f, etc) e o operador genérico %s funciona para
# todos os tipos.
#
#
# Exercícios 
# ----------
#
# 1) Agora faça um programa que imprime seu nome na tela e execute



