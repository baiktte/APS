import sys

sys.stdin = open("4843.txt", "r")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    lst = []
    number = sorted(numbers)
    num_min = 0
    num_max = N-1
    for n in range(N):
        # 리스트의 인덱스 홀수일 경우 작은 수 부터
        if n % 2 != 0:
            lst.append(number[num_min])
            num_min += 1
        # 리스트의 인덱스 짝수일 경우 큰수부터
        else:
            lst.append(number[num_max])
            num_max -= 1

    result = '#{} '.format(t)
    for i in range(10):
        result += str(lst[i])
        # 공백 마지막에 안넣기 위해
        if i != len(lst)-1:
            result += ' '

    print(result)





