import sys
sys.stdin = open("input2056.txt","r")

import datetime
T = int(input())

# 연월일 달력

for test_case in range(1,T+1):
    numbers= list(map(int, input().split()))

    result = 0
    for number in numbers:
        result+=





    
    
    print('#{} {}'.format(test_case, result))     


