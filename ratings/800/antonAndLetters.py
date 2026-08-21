# Problem: 443A - Anton and Letters
# Link: https://codeforces.com/problemset/problem/443/A
# Rating: 800
# Tags: implementation, constructive algorithms

import re

linha = re.split(r'[\s,{}]+', input())

unicos = set(linha) 

print(len(unicos) - 1)