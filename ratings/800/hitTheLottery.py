# Problem: 996A - Hit the Lottery
# Link: https://codeforces.com/problemset/problem/996/A
# Rating: 800
# Tags: dp, greedy

value = int(input())

notas = [100, 20, 10, 5, 1]
count = 0

## this solution works but it has time limit exceeded problem
## id = 0

## while (id < 5 and value > 0):
##    if value - notas[id] >= 0:
##        value -= notas[id]
##        count+=1
##    else:
##        id+=1

for nota in notas:
    count += value // nota
    value %= nota

print(count)
