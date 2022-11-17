import tempfile
# 파일을 임시로 만들어서 사용할 때 유용하다.

filename = tempfile.mkstemp() # 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다.
with tempfile.TemporaryFile() as f:
    f.write('asdf')
# TemporaryFile() : 임시 저장 공간으로 사용할 파일 객체를 반환한다.
# 기본적으로 바이너리 쓰기 모드(wb)를 갖는다.