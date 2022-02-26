====================
Prova de programação
====================


Os exercícios desta atividade possuem um formato comum baseado na criação de códigos pela permutação de linhas. O exemplo abaixo ilustra o funcionamento da atividade:

```python
"""
Crie um programa que peça dois números para o usuário e mostre o qual é o maior deles.

* if: 1
"""

print(f"o maior número é o a = {a}")
if a > b:
    a = int(input("a: "))
    elif b > a:
        if b > a:
            print(f"o maior número é o b = {b}")
            elif a > b:
                print(f"os números são iguais")
                else:
                    b = int(input("b: "))
```

O código acima possui todas as linhas necessárias para a resolução do problema proposto no enunciado da questão, mas embaralhadas em uma ordem aleatória e (provavelmente) com a indentação incorreta.

A solução é obtida modificando a ordem das linhas e (possivelmente o seu nível de indentação). Você não pode acrescentar novas linhas, mas é possível comentar ou apagar qualquer linha desenecessária. Em alguns casos, é necessário remover algumas linhas incorretas e, em outros, podem existir soluções corretas diferentes, cada uma baseada em um certo subconjunto de linhas.  

No exemplo acima, reorganizamos as linhas para obter a solução como mostrada abaixo:

```python
"""
Crie um programa que peça dois números para o usuário e mostre o qual é o maior deles.

* if: 1
"""

a = int(input("a: "))
b = int(input("b: "))
# if b > a:
if a > b:
    print(f"o maior número é o a = {a}")
# elif a > b:
elif b > a:
    print(f"o maior número é o b = {b}")
else:
    print(f"os números são iguais")
```

Observe que foi necessário comentar as linhas `if b > a` e `elif a > b`. Poderíamos resolver o problema de maneira alternativa trocando as condições utilizadas (`if a > b` e `elif b > a`) pelas linhas comentadas e trocando linha com os dois primeiros comandos `print`. 

A regra importante é que você não pode modificar o **conteúdo** de nenhuma linha, nem criar linhas novas ou duplicar alguma linha existente no código inicial. As únicas operações permitidas são modifiocar a **ordem** das linhas e o **nível de indentação**. 


Correção automática
===================

A atividade vem com um script responsável por realizar a correção automática de cada exercício. A correção é realizada pelo script "_corrigir.py" (note o underscore no início do nome). Podemos executá-lo como 

```
$ python _corrigir.py
```

para realizar a correção de todos os exercícios da prova. 

Podemos isolar exercícios específicos, passando-os como argumentos para o script:

```
$ python _corrigir.py pares zeros
```

Isso limita a correção a somente estes dois exercícios e facilita a leitura das mensagens de erro.


Avaliação/notas
===============

Cada exercício resolvido corretamente confere 1 ou mais pontos nas competências listadas logo abaixo do enunciado. No código de exemplo acima, teríamos somente um ponto conferido para a competência `if`. Vale lembrar que é necessário realizar 10 pontos por competência para demonstrar proficiência.


Organização dos arquivos
========================

O repositório consiste neste README, alguns arquivos.py correspondentes aos exercícios e alguns scripts de correção ou outras atividades auxiliares. Todos os scripts de uso interno, inclusive o de correção, são marcados com um "_" no início do nome. Os outros arquivos.py correspondem aos exercícios da prova.

O script de correção cria um arquivo chamado grades.json que pode ser ignorado ou apagado.
