import sys
with sys.stdin as i:
    n = int(i.readline().rstrip())
    for _ in range(n):
        x,y = [int(x) for x in i.readline().rstrip().split()]
        l = [[str(10) for i1 in range(20)] for i2 in range(20)]
        l[x][y] = '100'
        for r in range(max(0, (x - 1)), min(20, ((x + 1) + 1))):
            for c in range(max(0, (y - 1)), min(20, ((y + 1) + 1))):
                if l[r][c] == '10':
                    l[r][c] = '50'
        for r in range(max(0, (x - 2)), min(20, ((x + 2) + 1))):
            for c in range(max(0, (y - 2)), min(20, ((y + 2) + 1))):
                if l[r][c] == '10':
                    l[r][c] = '25'
        for line in l:
            print(' '.join(line))
