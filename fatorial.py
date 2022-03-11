# -*- coding: utf-8 -*-
"""
Crie um programa que peça um número e calcule o seu fatorial

* for: 1
"""

n = int(input("n: "))
fat = 1
for x in range(1, n + 1):
    fat *= x

print(f"fat({n}) = {fat}")

#fat *= x + 1
#fat = 0
#for i in range(n):
