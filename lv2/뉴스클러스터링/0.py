def mklist(s):
    s = s.upper()
    l = len(s)
    parts = []
    for i in range(l - 1):
        part = s[i:i + 2]
        for j in part:
            n = ord(j)
            if not 64 < n < 91:
                break
        else:
            parts.append(part)
    return parts

def mkdict(a, b):
    c = {}
    # 1. a안의 어떤 원소 i에 대해
    for i in a:
        # 2. 어떤 원소 i가 b에도 있으면
        if i in b:
            # 3. i를 키로 가지고
            # 4. 두 리스트에서 i의 개수를 센 것중 큰 수를 value로 가짐
            c[i] = max(a.count(i), b.count(i))
        else:
            # 5. 없으면 a.count(i)
            c[i] = a.count(i)
    return c

def union(c1, c2):
    c = {}
    for k, v in c1.items():
        if k not in c:
            c[k] = v
    for k, v in c2.items():
        if k not in c:
            c[k] = v
    return c

def inter(a, b):
    d = {}
    for i in a:
        if i in b:
            d[i] = min(a.count(i), b.count(i))
    return d

def solution(str1, str2):
    a = mklist(str1)
    b = mklist(str2)
    c1 = mkdict(a, b)
    c2 = mkdict(b, a)
    c = union(c1, c2)
    d = inter(a, b)
    if len(c) == 0 and len(d) == 0:
        return 65536
    a = []
    b = []
    for k, v in c.items():
        for _ in range(v):
            a.append(k)
    for k, v in d.items():
        for _ in range(v):
            b.append(k)
    return len(b) / len(a) * 65536 // 1

print(solution("aa1+aa2", "AAAA12"))