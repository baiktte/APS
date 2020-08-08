import sys
sys.stdin = open("1954.txt", "r")

T = int(input())

for t in range(1,T+1):
    print(f'{t}번째')
    N = int(input())
    bin_list = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            bin_list[i][j] =
