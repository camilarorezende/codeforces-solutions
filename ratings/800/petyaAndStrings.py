# Problem: 112A - Petya and Strings
# Link: https://codeforces.com/problemset/problem/112/A
# Rating: 800
# Tags: implementation, strings

palavra1 = input()
palavra2 = input()

palavra1 = palavra1.lower()
palavra2 = palavra2.lower()

if palavra1 == palavra2:
    print(0)
else:
    for i in range(0, len(palavra1)):
        if palavra1[i] > palavra2[i]:
            print(1)
            break
        elif palavra1[i] < palavra2[i]:
            print(-1)
            break
    


