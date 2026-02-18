# Problem: 281A - Word Capitalization
# Link: https://codeforces.com/problemset/problem/281/A
# Rating: 800
# Tags: implementation, strings

palavra = input()

resposta = ""
resposta += palavra[0].upper()
for letra in palavra[1:]:
    resposta += letra

print(resposta)