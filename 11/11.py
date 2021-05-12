import sys
with sys.stdin as line:
    n = int(line.readline().rstrip())
    for _ in range(n):
        width = int(line.readline().rstrip())
        for i in range(int(2**width) ):
            print("{:0>{width}}".format(bin(i)[2:], width=width))