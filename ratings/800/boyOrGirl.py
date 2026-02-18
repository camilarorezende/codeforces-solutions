# Problem: 236A - Boy or Girl
# Link: https://codeforces.com/problemset/problem/236/A
# Rating: 800
# Tags: implementation, strings, brute force

linha = input()

letras_distintas = []

for letra in linha:
    if letra not in letras_distintas:
        letras_distintas.append(letra)

if len(letras_distintas) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
