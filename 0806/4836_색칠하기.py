import sys

sys.stdin = open("4836.txt", "r")

T = int(input())


for t in range(1, T + 1):
    my = []
    test = int(input())

    # 빈 리스트 만들기 for문 마다 초기화
    bin_list = [[0 for _ in range(10)] for _ in range(10)]

    # test 갯수 만큼 x1, y1, x2, y2, color 할당
    for k in range(test):
        (x1, y1, x2, y2, color) = map(int, input().split())
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                bin_list[i][j] += color     # color를 더해줌 빨1 파2
    cnt = 0
    # 빈리스트 돌면서 3인 곳 카운팅
    for i in range(10):
        for j in range(10):
            if bin_list[i][j] == 3:
                cnt += 1

    print('#{} {}'.format(t, cnt))
