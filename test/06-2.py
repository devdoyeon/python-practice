result = []

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        result.append(i)

num = 0

for j in result:
    num += j

print(num)