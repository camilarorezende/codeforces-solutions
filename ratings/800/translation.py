# Problem: 41A - Translation
# Link: https://codeforces.com/problemset/problem/41/A
# Rating: 800
# Tags: implementation, strings

palavra1 = input()
palavra2 = input()

resposta = "YES"
if len(palavra1) == len(palavra2):
   for i in range(0, len(palavra1)):
       if palavra1[i] != palavra2[len(palavra1)-1-i]:
          resposta = "NO"
          break
else:
   resposta = "NO"

print(resposta)
