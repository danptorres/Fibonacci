def fibonacci(n):
    x = 0
    y = 1
    
    #sequência até que y seja maior ou igual a n
    while y < n:
        x, y = y, x + y
    
    #verifica se o número pertence à sequência de fibonacci
    if y == n or n == 0:
        return print(f"{n} pertence à sequência de Fibonacci.")
    else:
        return print(f"{n} Não pertence à sequência de Fibonacci.")

numero = int(input("Informe um número para análise: "))
fibonacci(numero)