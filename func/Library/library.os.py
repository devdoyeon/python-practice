import os
# 환경 변수나 Directory, File 등의 OS 자원을 제어할 수 있게 해주는 모듈이다.

print(os.environ) # environ({'SYSTEMD_EXEC_PID': '3410', …})
print(os.environ['PATH']) # '/usr/local/sbin:/usr/local/bin:/usr/sbin:/…'
os.chdir('/home/…') # 현재 Directory 위치를 변경한다.
print(os.getcwd) # 현재 Directory 위치를 알려준다. pwd와 비슷

os.system('pwd') # 시스템 명령어를 호출할 수 있다.
f = os.popen('pwd')
print(f.read()) # 시스템 명령어를 실행한 결괏값을 읽기 모드 형태의 파일 객체로 돌려준다.

os.mkdir('dir') # dir이라는 이름의 Directory를 생성한다.
os.rmdir('dir') # dir이라는 이름의 Directory를 삭제한다.
os.unlink('file.txt') # file.txt 파일을 삭제한다.
os.rename('file.txt', 'test.txt') # file.txt를 test.txt라는 이름으로 변경한다. 
