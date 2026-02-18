# Problem: 1030A - In Search of an Easy Problem
# Link: https://codeforces.com/problemset/problem/1030/A
# Rating: 800
# Tags: implementation, strings

qtd_pessoas = int(input())

linha = list(map(int, input().split()))

resposta = "EASY"
for num in linha:
    if num == 1:
        resposta = "HARD"

print(resposta)