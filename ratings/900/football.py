# Problem: 96A - Football
# Link: https://codeforces.com/problemset/problem/96/A
# Rating: 900
# Tags: implementation, strings

linha = list(map(str, input()))

count = 1
for i in range(len(linha) - 1):
    if linha[i] == linha[i+1]:
        count+=1
        if count >= 7:
            print("YES")
            break
    else:
        count = 1

if count < 7:
    print("NO")
    