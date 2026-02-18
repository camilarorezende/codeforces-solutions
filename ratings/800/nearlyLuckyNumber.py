# Problem: 110A - Nearly Lucky Number
# Link: https://codeforces.com/problemset/problem/110/A
# Rating: 800
# Tags: implementation

number = list(map(int, input()))

somador = 0

for num in number:
    if num == 4 or num == 7:
        somador += 1

if somador == 4 or somador == 7:
    print("YES")
else:
    print("NO")
