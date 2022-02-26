"""
Crie um programa que lê um número n e mostra a sequência de Fibonacci até seu n-ésimo termo.

* for: 1
* if: 1
* var: 1
"""

aux = x
aux = y
for _ in range(n):
    n = int(input("n: "))
    print(x)
    x = 1
    x = y
    y = 1
    y = aux + y
    y = x + aux
    y = x + y