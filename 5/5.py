import sys
with sys.stdin as i:
    cases = int(i.readline().rstrip())
    for _ in range(cases):
        cal1, cal5, size = [int(x) for x in i.readline().rstrip().split()]
        must_cal1 = size%5
        if must_cal1 == 0:
            must_cal1 = cal1
        if must_cal1>cal1:
            print('false')
            continue
        if cal1>6:
            cal1 -=must_cal1
            cal1_to_cal5 = int(cal1/5)
            cal5 += cal1_to_cal5
        if (must_cal1+(cal5*5))>= size:
            print('true')
        else:
            print('false')

