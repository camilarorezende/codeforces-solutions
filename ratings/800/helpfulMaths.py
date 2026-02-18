# Problem: 339A - Helpful Maths
# Link: https://codeforces.com/problemset/problem/339/A
# Rating: 800
# Tags: implementation, sortings, strings, greedy

linha = list(map(int, input().split("+")))

linha.sort()
resposta = ""

for i in range(len(linha) - 1):
    resposta += str(linha[i]) + "+"

resposta += str(linha[-1])

print(resposta)




