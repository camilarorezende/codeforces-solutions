# Problem: 344A - Magnets
# Link: https://codeforces.com/problemset/problem/344/A
# Rating: 800
# Tags: implementation

num = int(input())

lista = []
for i in range(num):
    ima = int(input())
    lista.append(ima)

count=0
for i in range(0, len(lista)-1):
    if lista[i] != lista[i+1]:
        count += 1

count+=1


print(count)
