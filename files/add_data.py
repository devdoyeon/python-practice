f = open('test.txt', 'a')
for i in range(11, 20):
    f.write(f'{i}번째 줄입니다.\n')
f.close()
