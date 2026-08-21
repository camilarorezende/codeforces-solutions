# Problem: 160A - TWins
# Link: https://codeforces.com/problemset/problem/160/A
# Rating: 900
# Tags: greedy, sortings

qtd = int(input())

moedas = list(map(int, input().split()))

metade = sum(moedas) / 2

moedas.sort(reverse=True)

total = 0
qtd = 0

for moeda in moedas:
    total+= moeda
    qtd+=1
    if total > metade:
        print(qtd)
        break


