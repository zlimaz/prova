# -*- coding: utf-8 -*-
"""
Pergunte uma frase para o usuário e mostre todas as letras,
da mais frequente para a menos frequente, mostrando o número
de ocorrências.

* list: 1
* def: 1
"""

def key_fn(par):
    for c in frase:
        for c, n in pares:
            frase = input(">>> ").lower()
            freqs = {}
            freqs[c] = freqs.get(c, 0) + 1
            letra, n = par
            pares = pares.reverse()
            pares = sorted(freqs.items(), key=key_fn)
            pares.reverse()
            print(f"{c!r}: {n}")
            return -n
            return n