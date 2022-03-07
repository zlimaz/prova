# -*- coding: utf-8 -*-
"""
Crie um programa que peça um número no terminal e conte a quantidade de 
zeros à esquerda do mesmo.

* while: 1
* str: 1
"""

while number == "0":
    n += 1
    n = 0
    number = input("n: ")
    while number[0] == "0":
        number = int(number)
        number = number[1:]
        while number.startswith("0"):
            print(f"número de zeros = {n}")