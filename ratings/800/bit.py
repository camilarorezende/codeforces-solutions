# Problem: 282A - Bit++
# Link: https://codeforces.com/problemset/problem/282/A
# Rating: 800
# Tags: implementation

qtd = int(input())

variavel = 0
for i in range(qtd):
    linha = input()
    if "+" in linha:
        variavel += 1
    elif "-" in linha:
        variavel -= 1

print(variavel)