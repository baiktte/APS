import sys
sys.stdin = open("input.txt","r")


T = int(input())

# 부등호 출력

for test_case in range(1,T+1):
    numbers= list(map(int, input().split()))
    result =''
    for number in numbers:
        if numbers[0]> numbers[1]:
            result ='>'
        elif numbers[0] == numbers[1]:
            result = '='
        elif numbers[0]< numbers[1]:    
            result = '<'    
    print('#{} {}'.format(test_case, result))     


