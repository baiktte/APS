import sys
sys.stdin = open('input_data/2050.txt')

# 'A'  65

# 알파벳을 숫자로 변환
my_list = []
T = input()
for t in T:
    my_list += t


result = []

for my in my_list:
    result += str(ord(my))

print(result)

