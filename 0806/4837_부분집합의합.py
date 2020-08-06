import sys

sys.stdin = open("4837.txt", "r")

T = int(input())


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
my = []
# 비트 연산자로 부분 집합 만들기
for i in range(1 << 12):
    my_arr = []
    for j in range(13):
        if i & (1 << j):
            my_arr.append(arr[j])
    my.append(my_arr)
print(my)


for t in range(1, T + 1):
    my_sum = 0
    [N, K] = list(map(int, input().split()))

    cnt = 0
    for i in my:
        if len(i) == N:
            if sum(i) == K:
                cnt += 1



    print('#{} {}'.format(t, cnt))
