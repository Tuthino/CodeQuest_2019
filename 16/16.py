import sys
def decode(string,key):
    output = []
    for i in range(1,65):
        string_chunk = string[(i*2)-2:(i*2)]
        key_chunk = key[(i*2)-2:(i*2)]
        num1 = int(string_chunk,16)
        num2 = int(key_chunk,16)
        decoded_num = (num1 ^ num2)
        output.append(chr(decoded_num))
    return ''.join(output)

with sys.stdin as i:
    n = int(i.readline().rstrip())
    for _ in range(n):
        cases = int(i.readline().rstrip())
        string = i.readline().rstrip()
        for _ in range(cases):
            key = i.readline().rstrip()
            decoded = (decode(string,key))
            print("[{}]".format(decoded))
