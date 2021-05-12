import sys
import math
obw_ziemi = 40075.
d_z = obw_ziemi/math.pi

with sys.stdin as i:
    n = int(i.readline().rstrip())
    for _ in range(n):
        r1 = float(i.readline().rstrip())
        D = d_z + (r1*2)
        circle = (math.pi*D)
        print(round(circle,1))
