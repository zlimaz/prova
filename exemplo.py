"""
Crie um programa que peça dois números para o usuário e mostre o qual é o 
maior deles.

* if: 0
"""

a = int(input("a: "))
b = int(input("b: "))
if b > a:
    print(f"o maior número é o b = {b}")
elif a > b:
    print(f"o maior número é o a = {a}")
else:
    print(f"os números são iguais")
# if a > b:
# elif b > a:
