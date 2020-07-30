import sys
sys.stdin = open("input2063.txt","r")
import math

T = int(input())

# 중간값 출력

for test_case in range(1,T+1):
    numbers= list(map(int, input().split()))
    number = sorted(numbers)
    
    num=number[len(number)//2]
        


    print('#{} {}'.format(test_case, num))     


