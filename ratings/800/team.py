# Problem: 231A - Team
# Link: https://codeforces.com/problemset/problem/231/A
# Rating: 800
# Tags: brute force, greedy

qtd = int(input())

somador = 0
for i in range(qtd):
    certezas = 0
    numeros = list(map(int, input().split()))
    for j in numeros:
        if j == 1:
            certezas += 1
            if certezas == 2:
                somador += 1

print(somador)

