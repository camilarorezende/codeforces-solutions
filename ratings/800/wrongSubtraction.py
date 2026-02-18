# Problem: 977A - Wrong Subtraction
# Link: https://codeforces.com/problemset/problem/977/A
# Rating: 800
# Tags: implementation

number, num_subs = map(int, input().split())

for i in range(num_subs):
    if str(number)[-1] != "0":
        number -= 1
    else:
        number = number // 10

print(number)