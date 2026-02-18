# Problem: 71A - Way Too Long Words
# Link: https://codeforces.com/problemset/problem/71/A
# Rating: 800
# Tags: strings

qtd = int(input())

palavras = []
for i in range(qtd):
    palavra = input()
    palavras.append(palavra)

resultado = []
for palavra in palavras:
    if len(palavra) > 10:
        palavra = palavra[0] + str(len(palavra) - 2) + palavra[-1]
        resultado.append(palavra)
    else:
        resultado.append(palavra)

for palavra in resultado:
    print(palavra)