import sys
sys.stdin = open("2789.txt", 'r')

word = sys.stdin.readline().rstrip()
ref = "CAMBRIDGE"

for s in word:
    if s in ref:
        word = word.replace(s, '')

print(word)