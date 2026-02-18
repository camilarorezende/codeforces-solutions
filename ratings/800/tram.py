# Problem: 116A - Tram
# Link: https://codeforces.com/problemset/problem/116/A
# Rating: 800
# Tags: implementation

qtd_paradas = int(input())

passageiros = 0
max = 0
for i in range(qtd_paradas):
    exit, enter = map(int, input().split())
    passageiros -= exit
    passageiros += enter
    if passageiros >= max:
        max = passageiros

print(max)
    