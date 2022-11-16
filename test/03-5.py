list = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
score = 0
result = 0

for i in list:
  score += i
  result = score / len(list)
print(result)