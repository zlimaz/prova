# -*- coding: utf-8 -*-
"""
Crie um programa que peça um número no terminal e conte a quantidade de 
zeros à esquerda do mesmo.

* while: 1
* str: 1
"""

number = input("n: ")

n=0

while number.startswith("0"): 
    number = number [1:]
    n += 1

print (f"numero de zeros = {n}")
