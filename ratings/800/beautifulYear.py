# Problem: 271A - Beautiful Year
# Link: https://codeforces.com/problemset/problem/271/A
# Rating: 800
# Tags: brute force

ano = int(input())

prox_ano = ano + 1

while(True):
    nums = str(prox_ano)
    if len(set(nums)) == 4:
        print(prox_ano)
        break
    prox_ano += 1