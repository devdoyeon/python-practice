import webbrowser
# 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈이다.

#= 웹 브라우저를 자동으로 실행하고 해당 URL인 google.com으로 가게 함
webbrowser.open('http://google.com')

#= 이미 웹 브라우저가 실행된 상태더라도 새로운 창으로 해당 주소가 열리게 함
webbrowser.open_new('http://google.com')