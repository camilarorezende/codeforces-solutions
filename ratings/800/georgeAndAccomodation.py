# Problem: 467A - George and Accommodation
# Link: hhttps://codeforces.com/problemset/problem/467/A
# Rating: 800
# Tags: implementation

rooms = int(input())

free = 0
for i in range(rooms):
    ocupation, capacity = map(int, input().split())
    if (capacity - ocupation >= 2):
        free += 1

print(free)