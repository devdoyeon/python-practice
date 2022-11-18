result = []

def GuGu(num):
    for i in range(10):
        if i == 0: continue
        result.append(num * i)
    print(result)

GuGu(5)