
#! iterable => 반복문을 돌릴 수 있는, 즉 반복이 가능한 자료형

#& all <=> any

#= all(iterable) - return bool
#- 모든 요소가 참이어야 True, 하나라도 거짓일 경우 False를 반환한다.
#- 입력 인수가 빈 값일 경우 True를 반환한다.
all([1, 2, 3, 4]) # True
all([1, 2, 3, 0]) # False

#= any(iterable) - return bool
#- 하나라도 참이면 True, 모든 요소가 거짓일 경우에만 False를 반환한다.
any([1, 0, 2, 3]) # True
any([0, 0, 0, 0]) # False

#& chr <=> ord

#= chr(Unicode) return Str
#- 유니코드를 입력 받아 그 코드에 해당하는 문자를 반환한다.
chr(97) # 'a'
chr(44032) # '가'

#= ord(str) - return Unicode
#- 문자열을 입력 받아 그 문자에 해당하는 유니코드를 반환한다.
ord('a') # 97
ord('가') # 44032

#& max <=> min

#= max(iterable) - return maxValue
max([1, 3, 6, 8, 10]) # 10
max('python') # 'y'

#= min(iterable) - return minValue
min([1, 3, 6, 8, 10]) # 1
min('python') # 'h'

#& =======================================================================

#= abs(Integer) - return 절댓값
abs(3) # 3
abs(-3) # 3

#= dir(any) - return Method
#- 객체가 자체적으로 가지고 있는 Method를 반환한다.
dir([1, 2, 3]) # ['append', 'count', 'extend', 'index', 'insert', 'pop',...]
dir({'1':'a'}) # ['clear', 'copy', 'get', 'has_key', 'items', 'keys',...]

#= divmod(intA, intB) - return Tuple
#- intA를 intB로 나눈 몫과 나머지를 Tuple 형태로 반환한다.
divmod(7, 3) # (2, 1)
divmod(9, 2) # (4, 1)

#= enumerate(list | Tuple | String) - return index & value
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
    # 0 'body'
    # 1 'foo'
    # 2 'bar'

#= eval(str) - return value
#- expression은 실행 가능한 문자열을 입력받아 문자열을 실행한 결괏값을 반환한다.
eval('1+2') # 3
eval("'hello'+'world'") # 'helloworld

#= filter(function_name, object) - return TrueValue
#- 자료형을 입력값으로 받아 함수를 돌렸을 때 참인 값을 반환한다.
def positive(x):
    return x > 0
list(filter(positive, [-1, 2, 4, -7])) # [2, 4]

#= hex(int) - return Hexadecimal(16진수)
hex(234) # 0xea
hex(3) # 0x3

#= id(object) - return reference
a = 3
id(a) # 135072304 (해당 객체의 고유 주소 값)

#= input(string) - return value
#- string에 prompt로 만들 내용을 적어준 후 사용자의 입력을 받아 반환한다.
b = input('Enter: ') # 사용자의 입력이 변수 b에 저장된다.

#= int(integer | float, [radix]) - return integer
#- 숫자를 입력했을 때 정수 형태로 돌려준다. 두 번째 인자로 진수를 넣어줄 수 있다.
int('5') # 5
int('5.2') # 5
int('1A', 16) # 16진수로 나타낸 1A = 26
int('11', 2) # 2진수로 나타낸 11 = 3

#= isinstance(instance, class_name) - return bool
#- 입력으로 받은 Instance가 그 Class의 Instance인지 판단하여 True, False를 반환한다.
class Person : pass
a = Person()
isinstance(a, Person) # True
b = 1
isinstance(b, Person) # False

#= len(object) - return integer
#- 입력값의 길이를 반환한다.
len('python') # 6
len([3, 5, 7, 8, 9]) # 5
len((1, 'd', 'b')) # 3

#= list(iterable) - return list
#- 반복 가능한 자료형을 입력받아 리스트로 만들어 반환한다.
list('python') # ['p', 'y', 't', 'h', 'o', 'n']
list((1, 2, 3)) # [1, 2, 3]
list([1, 2, 3, 4]) # [1, 2, 3, 4]

#= map(func, iterable) - return Result
list(map(lambda x: x*2, [3, 2, 1])) # [6, 4, 2]

#= oct(integer) - return OctalString(8진수 문자열)
oct(34) # '0o42'
oct(12345) # '0o30071'

#= open(fileName, [mode]) - return fileObject 
#- mode를 생략할 경우 Default 값인 읽기 전용 모드(r)로 파일 객체를 만들어 반환한다.
#- w: 쓰기 모드 | r: 읽기 모드 | a: 추가 모드 | b: 바이너리 모드
f = open('binary.txt', 'rb') # r + b = 바이너리 읽기 모드

#= pow(int, int) - return squareValue
pow(2, 4) # 16
pow(3, 5) # 243

#= range([start], stop, [step]) - return iterable
#- start: 시작점 | stop: 범위 종료값 | step: 숫자 사이의 거리
range(5) # 0, 1, 2, 3, 4
range(5, 10) # 5, 6, 7, 8, 9
range(0, 10, 2) # 0, 2, 4, 6, 8

#= round(number, [ndigits]) - return integer
#- 숫자를 입력 받아 두 번째 인자인 자릿수(ndigits)에 따라 반올림 해준다.
round(4.6) # 5
round(5.678, 2) # 5.68

#= sorted(iterable) - return list
#- list 자료형의 sort 함수와는 다른 개념이다. sort는 리스트 객체 그 자체를 정렬만 할 뿐 결과를 반환해 주지는 않는다.
sorted([3, 1, 2]) # [1, 2, 3]
sorted(['a', 'c', 'b']) # ['a', 'b', 'c']
sorted(['zero']) # ['e', 'o', 'r', 'z']
sorted((3, 2, 1)) # [1, 2, 3]

#= str(object) - return string
str(3) # '3'
str([1, 2, 3]) # '[1, 2, 3]'
str('hi'.upper()) # 'HI'

#= sum(iterable) - return totalValue
sum([1, 2, 3]) # 6
sum((5, 7, 8)) # 20

#= tuple(iterable) - return Tuple
tuple([1, 2, 3]) # (1, 2, 3)
tuple('abc') # ('a', 'b', 'c')

#= type(object) - return Type
type('abc') # <class 'str'>
type([1, 3, 5]) # <class 'list'>
type(open('test.txt', 'w')) # <class '_io.TextIOWrapper'>

#= zip(*iterable)
#- 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
list(zip([1, 2, 3], [4, 5, 6])) # [(1, 4), (2, 5), (3, 6)]
list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
list(zip("abc", "def")) # [('a', 'd'), ('b', 'e'), ('c', 'f')]