import sys
sys.stdin = open("1620.txt", 'r')
N, M = map(int, sys.stdin.readline().split())
pokemon_name = {}
pokemon_num = {}
for i in range(1, N + 1):
    name = sys.stdin.readline().strip()
    pokemon_name[name] = str(i)
    pokemon_num[str(i)] = name
for _ in range(M):
    q = sys.stdin.readline().strip()
    if q in pokemon_name:
        print(pokemon_name[q])
    else:
        print(pokemon_num[q])