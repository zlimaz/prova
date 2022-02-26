"""
Crie um programa que leia uma lista de strings separadas por vírgulas e
mostre uma lista de pares. Caso a lista possua um número ímpar de 
elementos, inclua a string vazia como segundo elemento do par final

* while: 1
* lst: 1
"""

else:
    for i in range(0, n, 2):
        for x, y in pares:
            if i == n - 1:
                n = len(pares)
                n = len(strings)
                pares = []
                pares.append([x, y])
                print(x, y)
                strings = input("lst: ").split(",")
                x = strings[i]
                y = ""
                y = strings[i + 1]