#!/usr/bin/env python
""" Imprime a tabuda de 1 ao 10.

---Tabuada do 1---
    1 x 1 = 1
    2 x 1 = 2
    3 x 1 = 3
 
 ...

 ###################
 ---Tabuada de 2----
    2 x 1 = 2
    2 x 2 = 4
    2 x 3 = 6

"""

__version__ = "0.1.2"
__author__ = "Italo"

template_base = """ 
  ---Tabuada de 2----

        {operacao}


"""
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Iterable (percorriveis)
numeros = list(range(1, 11))

# para cada numero em numeros:
for n1 in numeros:
    print()
    separacao = f" --- Tabuada de {n1} ---"
    print(separacao)
    print("#" * 30)
    print()
    for n2 in numeros:
        resultado = n1 * n2
        operacao = f"{n1} x {n2} = {resultado}" 
        print(operacao)
    #print(template.format(operacao=operacao))

