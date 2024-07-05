import sys
sys.stdin = open("10757.txt", 'r')

A, B = map(int, sys.stdin.readline().split())

print(A + B)