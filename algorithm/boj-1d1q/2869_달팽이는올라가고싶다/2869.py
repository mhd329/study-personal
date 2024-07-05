import sys
import math
sys.stdin = open("2869.txt", 'r')

A, B, V = map(int, sys.stdin.readline().split())

print(math.ceil((V - B) / (A - B)))