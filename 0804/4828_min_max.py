import sys
sys.stdin = open("input_data/4820.txt","r")

# 최대 최소 차이 구하기

T = int(input())

for t in range(1,T+1):
    num = int(input())
    numbers = list(map(int, input().split()))

    max_value = numbers[0]
    min_value = numbers[0]
    
    for number in numbers:
        if number >= max_value:
            max_value = number

        elif number <min_value:
            min_value = number 

    gap = max_value - min_value
    print('#{} {}'.format(t,gap))     
