# Problem: 50A - Domino Piling
# Link: https://codeforces.com/problemset/problem/50/A
# Rating: 800
# Tags: greedy, math

n, k = map(int, input().split())

tam = n * k

qtd_domino = tam // 2
print(qtd_domino)