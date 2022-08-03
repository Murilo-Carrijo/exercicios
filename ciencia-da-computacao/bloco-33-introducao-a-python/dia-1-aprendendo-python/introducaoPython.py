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
