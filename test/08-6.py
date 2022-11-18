input_area = input('숫자를 입력해 주세요.')
a = input_area.split(',')
num = 0

for i in a:
    num += int(i)
print(num)