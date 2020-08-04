# M개의 합의 max-min


import sys
sys.stdin = open("input_data/4835.txt","r")

T = int(input())

for t in range(1,T+1):
    box = list(map(int, input().split()))
    N = box[0]
    M = box[1]

    numbers = list(map(int, input().split()))
    
    max_value= 0
    min_value = 3000000
    value = 0
    
    for j in range(N-M+1):
        value = 0
        for i in range(M):
            value +=numbers[i+j]
        if max_value <= value:
            max_value = value
        if min_value >= value:
            min_value = value    
   
    gap = max_value - min_value


    print('#{} {}'.format(t,gap))     