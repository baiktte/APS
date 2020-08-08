import sys
sys.stdin = open("input2068.txt","r")
import math

T = int(input())

# 최댓값 출력

for test_case in range(1,T+1):
    numbers= list(map(int, input().split()))
    
    for number in numbers:
        max_value = max(numbers)
    print('#{} {}'.format(test_case, max_value))     


