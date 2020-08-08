import sys
sys.stdin = open("input_data/input2063.txt","r")
import math



# 중간값 출력

for test_case in range(1,2):
    T = int(input())
    numbers= list(map(int, input().split()))
    number = sorted(numbers)
   
    num=number[len(number)//2]
        


    print('{}'.format(num))     


