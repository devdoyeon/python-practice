import time
import threading
# 스레드를 사용하여 한 프로세스 안에서 2가지 또는 그 이상의 일을 수행할 수 있게끔 하는 모듈이다.

def long_task1(): # 25초의 시간이 걸리는 함수
    for i in range(5): # 5초가 걸림
        time.sleep(1)
        print(f'working:{i}\n')

print('Start')

for i in range(5): # 5초가 걸리는 함수를 5번 실행
    long_task1()

print('End')

#= 위와 같은 함수를

def long_task2():
    for i in range(5):
        time.sleep(1)
        print(f'working:{i}\n')

print('Start')

threads = []
for i in range(5):
    t = threading.Thread(target=long_task2)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join() # 해당 스레드가 종료될 때까지 기다리게 한다.

print('End')