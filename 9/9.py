import string
import sys
with sys.stdin as i:
    n = int(i.readline().rstrip())
    nums = ['0','1','2','3','4','5','6','7','8','9']
    lett = list(string.ascii_letters)
    for _ in range (n):
        line = i.readline().rstrip()
        if len(line)==0:continue
        count = 0
        hours='00'
        minutes='00'
        seconds='00'
        line = line.replace('and','').replace(',','').replace(' ','').strip()
        for letter in line:
            if letter in nums:
                count += 1
            if letter == 's':
                if count<2:
                    seconds='0'+str(line[:count])
                elif count == 0 : seconds='00'
                else:
                    seconds=str(line[:count])
                line = line[count+1:]
                count = 0
            if letter == 'm':
                if count<2:
                    minutes='0'+str(line[:count])
                elif count == 0: minutes ='00'
                else:
                    minutes=str(line[:count])
                line = line[count+1:]
                count = 0
            if letter == 'h':
                if count<2:
                    hours='0'+str(line[:count])
                elif count ==0 : hours ='00'
                else:
                    hours=str(line[:count])
                line = line[count+1:]
                count = 0
        print(hours+':'+minutes+':'+seconds)

