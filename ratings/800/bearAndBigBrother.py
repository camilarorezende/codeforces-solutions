# Problem: 791A - Bear and Big Brother
# Link: https://codeforces.com/problemset/problem/791/A
# Rating: 800
# Tags: implementation

anos = 0

limak, bob = map(int, input().split())

while(limak <= bob):
    limak = limak * 3
    bob = bob * 2
    anos += 1
    if limak > bob:
        break

print(anos)
