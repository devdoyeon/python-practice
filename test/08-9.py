num = 0

with open('sample.txt') as r:
    content = r.read()

for i in content.split('\n'):
    num += int(i)

average = num / len(content.split('\n'))

with open('result.txt', 'w') as w:
    w.write(f'{average}')