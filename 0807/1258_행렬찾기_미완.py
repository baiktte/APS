import sys

sys.stdin = open("1258.txt", "r")

# 행렬 = [세로][가로]
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    lst = []
    for i in range(N):
        lsts = list(map(int, input().split()))
        lst.append(lsts)

    cnt = 0
    count = []
    for i in range(N):
        cnt = 0
        for j in range(N):
            if lst[j][i] != 0:
                cnt += 1

            if lst[j][i] == 0:
                if cnt != 0:
                    count.append(cnt)
                cnt = 0


    # count의 최댓값+1 길이의 result 리스트를 만듬(0으로 초기화)
    result = [0] * (max(count) + 1)
    # 배열속 수를 result[수]에 축적
    for e in count:
        result[e] += 1
    my = []
    # 행과 열을 곱한 값이 가장 작은 순서 같을 경우 행이 작은순
    temp = result[0:len(result)]
    for i in range(len(temp)):
        temp[i] = i * temp[i]
    temp2 = []
    for i in temp:
        if i > 0:
            temp2.append(i)
    print('#{} {}'.format(t,len(temp2)), end=" ")
    while len(temp2) > 0:
        m = min(temp2)
        r = temp.index(m)
        c = result[r]
        print(r, c, end=" ")
        del temp2[temp2.index(m)]
    print()
    '''
    for i in range(1, len(result)):
        if result[i] != 0:
            my.append(i)
            my.append(result[i])
    my.insert(0, len(my) // 2)

    # 리스트에서 그냥 숫자로 꺼내기 위한 작업
    end = '#{} '.format(t)
    for i in range(len(my)):
        end += str(my[i])
        # 공백 마지막에 안넣기 위해
        if i != len(my) - 1:
            end += ' '

    print(end)
    '''
