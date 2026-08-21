# Problem: 318A - Even Odds
# Link: https://codeforces.com/problemset/problem/318/A
# Rating: 900
# Tags: math

#this solution has time limit exceeded

#num, pos = map(int, input().split())

#array_odd = []
#rray_even = []

#for i in range(1, num+1):
#    if i % 2 != 0:
#        array_odd.append(i)
#    else:
#        array_even.append(i)

#array_final = array_odd + array_even

#print(array_final[pos-1])

num, pos = map(int, input().split())

qtd_impares = (num+1) // 2

if pos <= qtd_impares:
    print(2 * pos - 1)
else:
    print(2 * (pos - qtd_impares))

