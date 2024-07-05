import sys
sys.stdin = open("25192.txt", 'r')

N = int(sys.stdin.readline())
log = set()
greeting = 0

for _ in range(N):
    nick = sys.stdin.readline().rstrip()
    log.add(nick)
    
    if nick == "ENTER":
        greeting += len(log) - 1
        log.clear()

greeting += len(log)
print(greeting)