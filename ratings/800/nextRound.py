# Problem: 158A - Next Round
# Link: https://codeforces.com/problemset/problem/158/A
# Rating: 800
# Tags: implementation, special problem

n, k = map(int, input().split())

qtd = 0

numeros = list(map(int, input().split()))
pivo = numeros[k-1]
for num in numeros:
    if num > 0 and num >= pivo:
        qtd += 1

print(qtd)