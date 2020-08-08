import sys

sys.stdin = open("1974.txt", "r")

T = int(input())

for t in range(1, T + 1):
    number = []
    for i in range(9):
        numbers = list(map(int, input().split()))
        number.append(numbers)

    # 겹치는 수가 없으면 1 겹치는 수가 있으면 0
    # result는 겹치는 수 있는지 없는지 확인해주는 값
    result = 0

    # 가로 확인
    for i in range(9):
        lst = []
        for j in range(9):
            lst.append(number[i][j])
        check = sorted(lst)
        if check != [1,2,3,4,5,6,7,8,9]:
            result+=1
        else:
            result+= 0
    # 세로 확인
    for i in range(9):
        lst = []
        for j in range(9):
            lst.append(number[j][i])
        check = sorted(lst)
        if check != [1,2,3,4,5,6,7,8,9]:
            result+=1
        else:
            result+= 0
    # 3*3 확인
    start = 0
    last =3
    # 3번 확인해줌
    for x in range(3):
        lst =[]
        # start,last의 간격 3임을 유지하며 3*3 확인
        for i in range(start, last):
            for j in range(start, last):
                lst.append(number[i][j])
        check = sorted(lst)
        start += 3
        last += 3
        if check != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            result += 1
        else:
            result+= 0

    # result가 0 이면 스토쿠가 올바르게 진행되어 1
    if result != 0:
        game = 0
    elif result == 0:
        game = 1

    print('#{} {}'.format(t, game))