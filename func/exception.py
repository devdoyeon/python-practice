class MyError(Exception):
    pass

for i in range(0, 5):
    try:
        4/i
    except ZeroDivisionError as e:
        print(e)
    else:
        print('pass')
    finally:
        print('finally')

'''
try - except - finally
try문 수행 중 오류가 발생하면 except문이 실행 되고,
오류가 발생하지 않았을 때 else문 실행,
오류 발생 여부와 관계 없이 finally문이 실행된다.
'''