# Problem: 266A - Queue at the School
# Link: https://codeforces.com/problemset/problem/266/B
# Rating: 800
# Tags: implementation, graph matchings, shortest paths, constructive algorithms

num_criancas, tempo = map(int, input().split())
linha = list(input())

for i in range (tempo):
    j = 0
    while j < num_criancas - 1:
        if linha[j] == "B" and linha[j+1] == "G":
           linha[j], linha[j+1] = linha[j+1], linha[j]
           j += 2
        else:
           j += 1  
      
print("".join(linha)) 