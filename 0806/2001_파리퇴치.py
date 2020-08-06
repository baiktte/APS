import sys

sys.stdin = open("2001.txt", "r")

T = int(input())

for t in range(1, T+1):
    my_arr = []
    (N, M) = map(int, input().split())

    sums = []
    # 파리표 만들기
    for i in range(N):
        arr = list(map(int, input().split()))
        my_arr.append(arr)
    # 최대 구하기 시작
    for x in range(N - M + 1):
        for y in range(N - M + 1):
            temp = 0
            for i in range(M):
                for j in range(M):
                    temp += my_arr[x+i][y+j]
            sums.append(temp)

    print('#{} {}'.format(t,max(sums)))