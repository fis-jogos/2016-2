# Definimos uma função fatorial de forma recursiva
def fat(x):
    return x * fat(x - 1) if x > 0 else 1
    
# Vejamos o resultado de alguns fatoriais (observe a precisão arbitrária):
for x in range(21):
    print('%s! = %s' % (x, fat(x)))
    
# Exercícios 
# ----------
#
# 1) Defina uma função que calcule os números de Fibonacci de forma recursiva.
#    Só lembrando: 
#        fib(0) = fib(1) = 1
#        fib(i) = fib(i - 1) + fib(i - 2)
#
