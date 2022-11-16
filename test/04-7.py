r = open('text.txt', 'r')
text = r.read()
r.close()

f = open('text.txt', 'w')
f.write(text.replace('java', 'python'))
f.close()