"""
Crie um programa que mostre uma lista com todos os primos de 1 até n, onde
n é um valor fornecido pelo usuário.

O exercício possui algumas dicas de implementação na forma de comentários.

* for: 2
"""

# Acrescentamos os novos primos à lista de primos.
# Assumimos que o número é primo e tentamos encontrar o divisor.
# Um número não pode ser primo se for divisível por outro primo.
for p in primos:
    for x in nums:
        if x % p == 0:
            if é_primo:
                n = int(input("n: "))
                nums = range(2, n + 1)
                nums = range(2, n)
                nums = range(n)
                primos = [2, 3]
                primos.append(x)
                print(primos)
                é_primo = False
                é_primo = True