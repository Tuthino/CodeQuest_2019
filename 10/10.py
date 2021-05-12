import sys
def cipher(char,key):
    num = ord(char)

    out_num = num-key
    if out_num > 122: out_num -= 26
    if out_num < 97: out_num += 26
    return chr(out_num)
with sys.stdin as i:
    n = int(i.readline().rstrip())
    for _ in range(n):
        key = int(i.readline().rstrip())
        string = list(i.readline().rstrip())
        for index in range(len(string)):
            if string[index] == " ": continue
            string[index] = cipher(string[index],key)
        print(''.join(string))