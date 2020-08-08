# 전기버스

import sys
sys.stdin = open("input_data/4831.txt","r")

T = int(input())

for t in range(1,T+1):
    my = list(map(int,input().split()))
    k = my[0]       # 최대 이동 정류장
    N = my[1]       # 종점
    M = my[2]       # 충전기 갯수

    busstop = list(map(int,input().split()))
    
    check = k
    cnt=0
    count=0
    for i in range(1,N+1):
        cnt+=1
        for bus in busstop:
            if cnt == check:
                count+=1
                check+=k
            if check >= busstop[i+1]:
                check = busstop[i+1]
    print(count)
















    # # for j in range(N):
    # #     for courese in courses:
    # #         count+=1
            
    # #         if count == result:
    # #             if courese == result:
    # #                 cnt+=1
                    
    # #             elif courses[result//k]> result:
    # #                 result = courese
    # #                 cnt+=1


    # for courese in courses:
    #     count+=1
            
    #     if courses[result//k]>= result:
    #         result = courese
    #         cnt+=1

    #     else:
    #         cnt=0   


    # print(cnt)                  