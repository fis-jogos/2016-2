# O Python possui suporte nativo para dicionários. O dicionário funciona como 
# um mapa entre chave --> valor, onde podemos facilmente resgatar o valor 
# associado a qualquer chave. Veja a sintaxe para definir um dicionário.
D = {'nome': 'Jesus', 'idade': 33, 'profissão': 'profeta'}

# Podemos acessar as chaves ou inserir novos pares usando a notação abaixo
nome = D['nome']
D['etnia'] = 'judeu'
    
# Veja como o dicionário se modificou
print(D)
    
# Exercícios
# ----------
#
# 1) Faça uma função cuja a entrada seja uma string e a saída seja um dicionário
#    mapeando cada caractere nesta string com o número de vezes que ele aparece
#    na palavra: ex.: 'palavra' --> {'p': 1, 'a': 3, 'l': 1, 'v': 1, 'r': 1}
#
# 2) Os dicionários possuem uma ordem bem definida? Converta vários dicionários 
#    para listas e experimente.
#
# 3) Os dicionários podem ser utilizados em laços. Utilize cada uma das formas
#    abaixo e explique a diferença.
#        for x in D:
#            ...
#        for x in D.values():
#            ...
#        for x in D.items():
#            ... 
