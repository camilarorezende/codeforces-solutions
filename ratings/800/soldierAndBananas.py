# Problem: 546A - Soldier and Bananas
# Link: https://codeforces.com/problemset/problem/546/A
# Rating: 800
# Tags: implementation, math, brute force

k, n, w = map(int, input().split())

total = 0
for i in range(1, w+1):
    total += (i * k)

emprestado = total - n

if emprestado > 0:
    print(emprestado)
else: 
    print(0)
