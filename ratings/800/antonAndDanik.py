# Problem: 734A - Anton and Danik
# Link: https://codeforces.com/problemset/problem/734/A
# Rating: 800
# Tags: implementation, strings

qtd = int(input())
linha = input()

anton = 0
danik = 0
for letra in linha:
    if letra == "A":
        anton += 1
    else:
        danik += 1

if anton == danik:
    print("Friendship")
elif anton > danik:
    print("Anton")
else:
    print("Danik")