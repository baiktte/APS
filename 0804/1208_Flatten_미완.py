import sys
sys.stdin = open('input_data/1208.txt')

for i in range(1,11):
    dump_cnt = int(input())
    dump_list = list(map(int, input().split()))

    max_value = 0
    min_value = 100
    count=0

    while count <= dump_cnt:
        for i in range(99):
            if dump_list[i] > max_value:
                max_value = dump_list[i]
                

            if dump_list[i] < min_value:
                min_value = dump_list[i]

    
    
    gap = max_value - min_value
        
    
         