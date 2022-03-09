# -*- coding: utf-8 -*-
"""
Crie um programa que mostre uma lista com todos os primos de 1 até n, onde
n é um valor fornecido pelo usuário.

O exercício possui algumas dicas de implementação na forma de comentários.

* for: 2
"""

# Acrescentamos os novos primos a lista de primos.
# Assumimos que o numero e primo e tentamos encontrar o divisor.
# Um numero nao pode ser primo se for divisivel por outro primo.
e_primo = False
e_primo = True
for p in primos:
    for x in nums:
        if e_primo:
            if x % p == 0:
                n = int(input("n: "))
                nums = range(2, n + 1)
                nums = range(2, n)
                nums = range(n)
                primos = [2, 3]
                primos.append(x)
                print(primos)