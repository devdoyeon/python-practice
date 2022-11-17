import shutil
# 파일을 복사해 주는 모듈이다.

shutil.copy('src.txt', 'dst') # src.txt라는 이름의 파일을 dst로 복사하고,
# 동일한 파일 이름이 있을 경우에는 덮어쓴다.