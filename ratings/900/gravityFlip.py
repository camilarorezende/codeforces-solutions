# Problem: 405A - Gravity Flip
# Link: https://codeforces.com/problemset/problem/405/A
# Rating: 900
# Tags: greedy, implementation, sortings

#this solution is more complex
#n = int(input())

#cubos = list(map(int, input().split()))

#for i in range(n):
#    for j in range(i + 1, n):
#        if cubos[i] > cubos[j]:
#            cubos[i], cubos[j] = cubos[j], cubos[i]
#
#print(*cubos)

n = int(input())

cubos = list(map(int, input().split()))

cubos.sort()

print(*cubos)
