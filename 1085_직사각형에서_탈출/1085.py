import sys
sys.stdin = open("1085.txt", 'r')

x, y, w, h = map(int, sys.stdin.readline().split())

a = w - x if w - x < h - y else h - y
b = x if x < y else y

print(a if a < b else b)