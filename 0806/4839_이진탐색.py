import sys

sys.stdin = open("4839.txt", "r")

T = int(input())

for t in range(1, T + 1):
    (p, a, b) = list(map(int, input().split()))

    first = 1
    last = p
    mid = 0
    a_cnt = 0
    b_cnt = 0
    result = ''

    # while로 이진탐색
    while 1 <= last-1:
        mid = (first+last)//2
        if mid == a:
            a_cnt+=1
            break
        elif mid > a:
            last = mid
            a_cnt += 1
        else:
            first = mid
            a_cnt += 1

    # b 이진 탐색하기 전 초기화!
    first = 1
    last = p
    mid = 0
    while 1 <= last-1:
        mid = (first+last)//2
        if mid == b:
            b_cnt+=1
            break
        elif mid > b:
            last = mid
            b_cnt += 1
        else:
            first = mid
            b_cnt += 1

    if a_cnt > b_cnt:
        result = 'B'
    elif a_cnt == b_cnt:
        result = '0'
    else:
        result = 'A'

    print('#{} {}'.format(t,result))

