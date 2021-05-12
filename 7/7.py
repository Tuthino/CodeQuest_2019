import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    count = int(sys.stdin.readline().rstrip())
    l = [float(sys.stdin.readline().rstrip()) for x in range(count)]
    lmin, lmax = min(l), max(l)
    for i in l:
        print(int(round((i - lmin)/(lmax-lmin)*255)))
