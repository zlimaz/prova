"""
Crie um programa que peça um número inteiro no terminal mostre o maior 
digito do mesmo.

* while: 1
* int: 1
"""

m = 0
m = m // 10
m = max(unidade, m)
while n > 0:
    n = int(input("n: "))
    n = n // 10
    print(f"maior dígito = {m}")
    unidade = n % 10
