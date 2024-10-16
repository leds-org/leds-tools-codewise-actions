# Imports desnecessários
import math
import os
import random
import datetime

# Variáveis globais
x = 10
y = 20
result = 0

# Função sem propósito claro
def process_data():
    global x, y, result
    result = x + y
    if result > 15:
        print("Resultado maior que 15")
    else:
        print("Resultado menor ou igual a 15")
    return x * y + random.randint(1, 100)

# Função muito longa com múltiplas responsabilidades
def long_function():
    global result
    for i in range(10):
        if i % 2 == 0:
            print("Número par:", i)
        else:
            print("Número ímpar:", i)

        # Cálculo desnecessário dentro do loop
        temp = 0
        for j in range(100):
            temp += j * i
        
        # Código duplicado
        if i % 3 == 0:
            print("Número divisível por 3:", i)
        else:
            print("Número não divisível por 3:", i)
    
    process_data()
    
    # Concatenação de strings ineficiente
    text = ""
    for i in range(10):
        text += "Número " + str(i) + ", "
    
    print(text)

# Função sem tratamento de erros adequado
def read_file(filename):
    file = open(filename, 'r') # Não usa 'with'
    data = file.readlines()
    file.close()
    return data

# Função que faz tudo
def magic_function(a, b, c):
    # Usa variáveis globais sem necessidade
    global result
    if a > b:
        return process_data()
    elif b > c:
        return read_file("arquivo.txt")
    else:
        result = a + b + c
        print("Resultado é:", result)
        if result < 50:
            return random.randint(1, result)
        else:
            return result

# Nomes de variáveis ruins
def f(x, y, z):
    return x*y + z/x - y

# Função que quebra boas práticas de retorno
def validate_input(value):
    if type(value) != int:
        print("Valor inválido")
        return
    if value < 0:
        print("Valor negativo")
        return False
    else:
        print("Valor válido")
        return True

# Função que faz nada
def do_nothing():
    pass

# Função recursiva sem caso base correto
def broken_recursion(n):
    if n <= 0:
        return n
    else:
        return n + broken_recursion(n-1)

# Função gigante sem separação de lógica
def massive_calculation():
    global result
    total = 0
    for i in range(100):
        for j in range(100):
            total += i * j
    result = total
    print("Total calculado:", total)

    if total > 5000:
        return "Maior que 5000"
    elif total == 5000:
        return "Igual a 5000"
    else:
        return "Menor que 5000"

    # Código nunca executado
    print("Fim da função")

# Função que chama outras funções de forma confusa
def main():
    process_data()
    long_function()
    read_file("arquivo.txt")
    magic_function(3, 5, 7)
    f(2, 4, 6)
    validate_input(-1)
    broken_recursion(5)
    do_nothing()
    massive_calculation()
    print("Programa finalizado")

# Chamando a função principal
main()
