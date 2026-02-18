# Problem: 266A - Stones on the Table
# Link: https://codeforces.com/problemset/problem/266/A
# Rating: 800
# Tags: implementation

qtd_stones = int(input())
stones = list(map(str, input()))

num = 0
for i in range(0, qtd_stones-1):
    if stones[i] == stones[i+1]:
        num += 1

print(num)
    