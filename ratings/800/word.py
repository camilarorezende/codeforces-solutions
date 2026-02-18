# Problem: 59A - Word
# Link: https://codeforces.com/problemset/problem/59/A
# Rating: 800
# Tags: implementation, strings

palavra = input()

uppers = 0
lowers = 0

for letra in palavra:
    if letra == letra.upper():
        uppers += 1
    else:
        lowers += 1

if uppers == lowers or lowers > uppers:
    print(palavra.lower())
else:
    print(palavra.upper())
