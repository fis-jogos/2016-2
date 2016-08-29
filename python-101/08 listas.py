# O objetivo é criar a lista com os 20 primeiros números de Fibonacci.
# Começamos com os primeiros números.
L = [1, 1] 

# As listas são acessadas usando a notação L[i]. Podemos acessar ou modificar
# os elmentos da lista, lembrando que os índices começam a partir do zero:
#
#   L[0] --> primeiro elemento
#   L[1] --> segundo elemento
#   etc.

for i in range(20):
    # As listas também podem ser acessadas pelo fim: L[-1] representa o último
    # elemento, L[-2] o penúltimo, etc.
    next = L[-1] + L[-2]

    # O método .append() das listas permite acrescentar um elemento ao final
    # No 
    L.append(next)

# A função map(func, seq) retorna uma lista correspondente à aplicação de func
# à todos os elementos da seq. No caso, queremos converter uma lista de números
# em uma lista de strings e unir o resultado.
fibo_str = ', '.join(map(str, L))

# Agora imprimimos o resultado
print('20 primeiros números de Fibonacci')
print('---------------------------------')
print('\n%s' % fibo_str)
    
    
# Exercícios
# ----------
#
# 1) Crie um programa que pergunte 5 números para o usuário, salve-os numa lista
#    e imprima a média e o desvio padrão.
#
    
