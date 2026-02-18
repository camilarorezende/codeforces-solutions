# Problem: 486A - Calculation Function
# Link: https://codeforces.com/problemset/problem/486/A
# Rating: 800
# Tags: implementation, math

num = int(input())

resultado = 0

pares = num // 2
impares = num - pares 
 
soma_pares = 2 * (pares * (pares + 1) // 2)
soma_impares = impares * impares

resultado = soma_pares - soma_impares
print(resultado)
    
    