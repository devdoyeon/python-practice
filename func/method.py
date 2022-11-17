
#= abs(Integer) - return 절댓값
abs(3) # 3
abs(-3) # 3

#! all <=> any

#= all(반복 가능한 자료형(반복문을 돌릴 수 있는 자료형)) - return bool
#- 모든 요소가 참이어야 True, 하나라도 거짓일 경우 False Return
#- 입력 인수가 빈 값일 경우 True Return
all([1, 2, 3, 4]) # True
all([1, 2, 3, 0]) # False

#= any(반복 가능한 자료형) - return bool
#- 하나라도 참이면 True, 모든 요소가 거짓일 경우에만 False Return
any([1, 0, 2, 3]) # True
any([0, 0, 0, 0]) # False

#= chr(Unicode) return Str
#- 유니코드를 입력 받아 그 코드에 해당하는 문자를 출력함
chr(97) # 'a'
chr(44032) # '가'

#= dir(any) - return Method
#- 객체가 자체적으로 가지고 있는 Method를 보여줌
dir([1, 2, 3]) # ['append', 'count', 'extend', 'index', 'insert', 'pop',...]
dir({'1':'a'}) # ['clear', 'copy', 'get', 'has_key', 'items', 'keys',...]

#= divmod(intA, intB) - return Tuple
#- intA를 intB로 나눈 몫과 나머지를 Tuple 형태로 돌려줌
divmod(7, 3) # (2, 1)
divmod(9, 2) # (4, 1)

#= enumerate(list | Tuple | String) - return index & value
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
    # 0 'body'
    # 1 'foo'
    # 2 'bar'

#= eval(str) - return value
#- expression은 실행 가능한 문자열을 입력받아 문자열을 실행한 결괏값을 돌려줌
eval('1+2') # 3
eval("'hello'+'world'") # 'helloworld

#= filter(function_name, object) - return 