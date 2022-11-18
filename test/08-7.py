num = input('구구단을 출력할 숫자를 입력하세요. (2~9):')
a = []

for i in range(1, 10):
    a.append(int(num) * i)

print(a)