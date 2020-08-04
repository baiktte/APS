# 숫자카드 

import sys
sys.stdin = open("input_data/4834.txt","r")

T = int(input())

for t in range(1,T+1):
    N = int(input())
    num_list = list(map(int, input()))
    
    max_num =-1
    max_count = 0

    for i in range(10):
        if num_list.count(i) >= max_count:
            max_count = num_list.count(i)
            max_num =i


    print('#{} {} {}'.format(t,max_num, max_count))          