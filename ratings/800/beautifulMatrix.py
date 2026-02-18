# Problem: 263A - Beautiful Matrix
# Link: https://codeforces.com/problemset/problem/263/A
# Rating: 800
# Tags: implementation

qtd = 0

for i in range(5):
    numeros = list(map(int, input().split()))
    if 1 in numeros:
        if i == 0 or i == 4:
            qtd += 2
            if numeros[0] == 1 or numeros[4] == 1:
                qtd += 2
            elif numeros[1] == 1 or numeros[3] == 1:
                qtd += 1
        elif i == 1 or i == 3:
            qtd += 1
            if numeros[0] == 1 or numeros[4] == 1:
                qtd += 2
            elif numeros[1] == 1 or numeros[3] == 1:
                qtd += 1
        elif i == 2:
            if numeros[0] == 1 or numeros[4] == 1:
                qtd += 2
            elif numeros[1] == 1 or numeros[3] == 1:
                qtd += 1

print(qtd)