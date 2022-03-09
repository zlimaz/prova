# -*- coding: utf-8 -*-
"""
Crie um programa que leia uma lista de números inteiros e forneça o valor e posição do maior
elemento.

* for: 1
* if: 1
"""

def maxarg(lst):
    for i, x in enumerate(lst):
        if not lst:
            if x > max_value:
                max_pos = 0
                max_pos = i
                max_value = lst[0]
                max_value = x
                ns = [int(x) for x in input("ns: ").split(",")]
                pos, valor = maxarg(ns)
                print(f"maior valor = {valor}, posicao = {pos + 1}o")
                return (max_pos, max_value)
                return None