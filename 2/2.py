import sys
cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    num1,num2 = [int(x) for x in sys.stdin.readline().rstrip().split()]
    if num1 == num2:
        print((num2+num1)*2)
    else:
        print(num2+num1)