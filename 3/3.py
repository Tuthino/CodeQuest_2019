import sys
with sys.stdin as i:
    n = i.readline().rstrip()
    for _ in range(int(n)):
        g1, g2 = [x for x in i.readline().split()]
        if g1 == 'true' and g2 == 'true':
            print('true')
        elif g1 == 'false' and g2 == 'false':
            print('true')
        else:
            print('false')
