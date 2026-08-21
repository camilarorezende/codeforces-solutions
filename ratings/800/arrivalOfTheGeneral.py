# Problem: 144A - Arrival Of The General
# Link: https://codeforces.com/problemset/problem/144/A
# Rating: 800
# Tags: implementation

qtd = int(input())

count = 0

array = list(map(int, input().split()))

maior = max(array)
menor = min(array)

indice_menor = qtd - 1 - array[::-1].index(menor)

while (array[qtd-1] != menor):
    
    array[indice_menor], array[indice_menor+1] = array[indice_menor+1], array[indice_menor]
    indice_menor+=1
    count+=1

indice_maior = array.index(max(array))

while (array[0] != maior):
    
    array[indice_maior-1], array[indice_maior] = array[indice_maior], array[indice_maior-1]
    indice_maior-=1
    count+=1

print(count)
