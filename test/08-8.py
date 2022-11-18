with open('abc.txt') as f:
    content = f.readlines()

content.reverse()

with open('abc.txt', 'w') as f:
    for line in content:
        line = line.strip()
        f.write(f'{line}\n')