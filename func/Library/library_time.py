import time
# 시간과 관련된 모듈이다.

#= UTC(Universal Time Coordinated)를 사용하여 현재 시간을 실수 형태로 반환해 준다.
#= 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 반환한다.
print(time.time()) # 1668664015.22346

#= time.time()이 반환한 실수 값을 이용하여 연도, 월, 일, 시, 분, 초, ... 의 형태로 반환해 준다.
print(time.localtime(time.time())) # time.struct_time(tm_year=2022, tm_mon=11, 
# tm_mday=17, tm_hour=14, tm_min=48, tm_sec=24, tm_wday=3, tm_yday=321, tm_isdst=0)

#= time.localtime()에 의해 반환된 Tuple Type의 값을 인수로 받아 날짜와 시간을 반환한다.
print(time.asctime(time.localtime(time.time()))) # Thu Nov 17 14:49:28 2022

#= time.asctime(time.localtime(time.time())) 을 간편하게 표시할 수 있다.
#= 항상 현재 시간만을 돌려준다.
print(time.ctime()) # 'Thu Nov 17 14:50:40 2022'

#= 시간에 관계된 것을 세밀하게 표현하는 포맷 코드를 함께 입력해 시간을 표시할 수 있다.
'''
포맷코드	설명	예
%a	요일 줄임말	Mon
%A	요일	Monday
%b	달 줄임말	Jan
%B	달	January
%c	날짜와 시간을 출력함	06/01/01 17:22:21
%d	날(day)	[01,31]
%H	시간(hour)-24시간 출력 형태	[00,23]
%I	시간(hour)-12시간 출력 형태	[01,12]
%j	1년 중 누적 날짜	[001,366]
%m	달	[01,12]
%M	분	[01,59]
%p	AM or PM	AM
%S	초	[00,59]
%U	1년 중 누적 주-일요일을 시작으로	[00,53]
%w	숫자로 된 요일	[0(일요일),6]
%W	1년 중 누적 주-월요일을 시작으로	[00,53]
%x	현재 설정된 로케일에 기반한 날짜 출력	06/01/01
%X	현재 설정된 로케일에 기반한 시간 출력	17:22:21
%Y	년도 출력	2001
%Z	시간대 출력	대한민국 표준시
%%	문자	%
%y	세기부분을 제외한 년도 출력	01
'''
print(time.strftime('%a', time.localtime(time.time()))) # 'Thu'

#= 일정 시간 간격을 둘 수 있는 함수이다. loop 내에서 자주 사용된다.
#= 인수로 들어가는 값은 초(sec)단위이다.
for i in range(10):
    print(i)
    time.sleep(1)