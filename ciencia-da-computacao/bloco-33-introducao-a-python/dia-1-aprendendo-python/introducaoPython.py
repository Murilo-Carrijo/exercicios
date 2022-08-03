from math import ceil
# 🚀 Exercício 1: Crie uma função que receba dois números e retorne o maior deles.

def higherNumber(x, y):
    if x > y:
        return x
    return y


higherNumber(2, 3)

# 🚀 Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.

def average(listNumbers):
    sum = 0
    for number in listNumbers:
        sum += number
    return sum / len(listNumbers)

 
numbers = [10, 20, 30]
average(numbers)

# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1, imprima na tela um quadrado feito de asteriscos de lado de tamanho n. Por exemplo

def squaresDrawing(n):
    for row in range(n):
        print(n * '*')


squaresDrawing(5)

# 🚀 Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres. Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"], o retorno deve ser "Fernanda".

def biggestName(names):
    firstName = names[0]
    for name in names:
        if len(name) > len(firstName):
            firstName = name
    return firstName


names = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]
biggestName(names)

# Exercício 5: Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Crie uma função que retorne dois valores em uma tupla contendo a quantidade de latas de tinta a serem compradas e o preço total a partir do tamanho de uma parede(em m²).

def calcBuyPaint(mSquare):
    qtyCans = ceil(mSquare / 3)
    totalPrice = qtyCans * 80
    print(f'Quantidade: {qtyCans}', f'Valor: {totalPrice}')
    return f'Quantidade: {qtyCans}', f'Valor: {totalPrice}'


calcBuyPaint(50)

# Exercício 6: Crie uma função que receba os três lado de um triângulo e informe qual o tipo de triângulo formado ou "não é triangulo", caso não seja possível formar um triângulo.

def checkingTriangle(s1, s2, s3):
    check1 = s1 + s2
    check2 = s1 + s3
    check3 = s2 + s3
    if check1 > s3 and check2 > s2 and check3 > s1:
        if s1 == s2 == s3:
            print("Triângulo Equilátero")
        elif s1 == s2 or s1 == s3 or s2 == s3:
            print("Triângulo Isósceles")
        else:
            print("Triângulo Escaleno")
    else:
        print("Não é um triângulo")

checkingTriangle(10, 4, 2)