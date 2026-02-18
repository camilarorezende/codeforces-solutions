# Problem: 617A - Elephant
# Link: https://codeforces.com/problemset/problem/617/A
# Rating: 800
# Tags: math

coordenada = int(input())

steps = 0

while (coordenada >= 5):
    coordenada -= 5
    steps += 1
    if(coordenada < 5):
        break

if (coordenada > 0):
   steps += 1

print(steps)



