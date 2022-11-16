content = input('메모장에 입력할 내용: ')
f1 = open('text.txt', 'a')
f1.write(content)
f1.close()