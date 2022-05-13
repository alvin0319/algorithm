a, b, c = map(lambda x: int(x), input().split())

if b >= c:
    print(-1)
else:
    print(int((a // (c - b) + 1)))
