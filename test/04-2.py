def calcFn(*args):
    result = 0
    for i in args:
        result += i
    print(result / len(args))