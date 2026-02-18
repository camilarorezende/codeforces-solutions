# Problem: 677A - Vanya and Fence
# Link: https://codeforces.com/problemset/problem/677/A
# Rating: 800
# Tags: implementation

num_amigos, altura_max = map(int, input().split())
alturas = list(map(int, input().split()))

largura = 0

for num in alturas:
    if num > altura_max:
        largura += 2
    else:
        largura += 1

print(largura)